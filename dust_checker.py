import requests

FLIPSIDE_URL = "https://api.flipsidecrypto.com/api/v2/queries/9fe973d5-ea06-493a-b5a5-3b92f7880e7c/data/latest"

def get_helius_transfers(tx_ids, helius_api_key):
    url = f"https://api.helius.xyz/v0/transactions?api-key={helius_api_key}"
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    response = requests.post(url, headers=headers, json={"transactions": tx_ids})

    if response.status_code != 200:
        raise Exception(f"Helius error: {response.text}")

    transfers = []
    for tx in response.json():
        tx_id = tx.get("signature")
        for transfer in tx.get("nativeTransfers", []):
            transfers.append({
                "tx_id": tx_id,
                "from": transfer["fromUserAccount"],
                "to": transfer["toUserAccount"],
                "amount": transfer["amount"]
            })
    return transfers

def get_duster_wallets():
    response = requests.get(FLIPSIDE_URL)
    if response.status_code != 200:
        raise Exception(f"Flipside error: {response.text}")
    return {row["DUSTER_WALLET"] for row in response.json()}

def check_tx_dusting(tx_ids, helius_api_key):
    print("Pulling Helius data...")
    transfers = get_helius_transfers(tx_ids, helius_api_key)
    senders = [t["from"] for t in transfers]

    print("Getting duster wallets from Flipside...")
    duster_wallets = get_duster_wallets()

    print("\nChecking transfers:")
    results = {}
    for tx_id in tx_ids:
        tx_senders = [t["from"] for t in transfers if t["tx_id"] == tx_id]
        is_dusting = any(sender in duster_wallets for sender in tx_senders)
        results[tx_id] = is_dusting
        print(f"  {tx_id}: {'DUSTING' if is_dusting else 'clean'}")

    return results

# 🔍 Example usage
if __name__ == "__main__":
    tx_ids_to_check = [
        "3dKq8PUWK6wT1EJAq3im4x2jB2eWhDTzznfj15aQpLWtFYmRMsxeU8wdRmbHmF6mhgiT8NBtfHdGjJ3kH6ot9QFs"
    ]
    helius_key = "your-helius-api-key-here"  # Pass this in however you want
    check_tx_dusting(tx_ids_to_check, helius_key)

