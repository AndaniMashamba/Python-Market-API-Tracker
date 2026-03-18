 Python-Market-API-Tracker
Automated live cryptocurrency market tracker using REST APIs and Python. Generates real-time JSON log reports.
Automated Cryptocurrency API Tracker 

 Overview:
An automated data retrieval tool that interfaces with the CoinGecko REST API to monitor real-time market fluctuations. This project demonstrates the ability to manage live data streams, parse complex JSON objects, and generate timestamped logs for financial or operational monitoring.

 Key Features:
1. Live Market Integration: Fetches real-time price data and 24-hour percentage changes for Bitcoin, Ethereum, and Solana.

2. Network-Aware Engineering: Includes custom SSL-bypass logic using `urllib3` to ensure connectivity in restricted institutional or corporate network environments.

3. Automated Data Persistence: Generates structured `market_log.json` files, simulating a real-world "Heartbeat" monitoring system.

Tech Stack:
Language: Python 3.x
Libraries: `requests`, `urllib3`, `json`, `datetime`
Concepts: REST API Integration, JSON Parsing, Data Automation, Error Handling.
