# 🧹 Real-Time Solana Domain-Based Dusting Detector

Detect **domain-based dusting activity** in Solana transactions using real-time data.

- ✅ Uses Helius API to decode transaction transfer activity
- ✅ Cross-checks senders against Flipside's live dusting wallet list
- ✅ Flags transactions as `DUSTING` or `clean`

---

## 🛠 Setup

```bash
git clone https://github.com/jms1192/dust-tx_checker.git
cd dusting-detector
pip install -r requirements.txt
