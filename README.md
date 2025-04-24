# 🧹 Real-Time Solana Domain-Based Dusting Detector

Detect **domain-based dusting activity** in Solana transactions using real-time data.

- ✅ Built for **real-time dusting detection**
- ✅ Uses Helius API to decode transaction transfer activity
- ✅ Cross-checks senders against **Flipside's live dusting wallet list**
- ✅ Flags transactions as `DUSTING` or `clean`
- ✅ List of dusters reflects the **current set of active attackers**

---
## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## 🛠 Setup

```bash
git clone https://github.com/jms1192/dust-tx_checker.git
cd dusting-detector
pip install -r requirements.txt
