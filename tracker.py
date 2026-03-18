import requests
import json
import urllib3
from datetime import datetime

# Disable SSL warnings for the university network environment
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_crypto_prices():
    print("🌐 Fetching live market data from CoinGecko...")
    
    # API Endpoint for Bitcoin, Ethereum, and Solana
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd&include_24hr_change=true"
    
    try:
        # Fetching data with SSL bypass (verify=False) for network compatibility
        response = requests.get(url, timeout=15, verify=False)
        data = response.json()
        
        # Structure the report metadata
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report_data = {
            "report_time": timestamp,
            "market_data": data
        }

        # --- PRINT THE DASHBOARD ---
        print("\n" + "="*40)
        print(f"💰 LIVE CRYPTO MARKET TRACKER")
        print(f"📅 Last Updated: {timestamp}")
        print("="*40)

        for coin, info in data.items():
            price = info['usd']
            change = info['usd_24h_change']
            # Determine trend emoji
            trend = "📈" if change > 0 else "📉"
            print(f"{coin.upper():<10} | Price: ${price:>12,.2f} | 24h: {trend} {change:.2f}%")

        print("="*40)

        # --- SAVE THE AUTOMATED LOG ---
        # This keeps a record of the price at the moment the script was run
        filename = "market_log.json"
        with open(filename, "w") as file:
            json.dump(report_data, file, indent=4)
        
        print(f"\n✅ Automated report saved to: {filename}")

    except Exception as e:
        print(f"❌ Error tracking prices: {e}")

if __name__ == "__main__":
    get_crypto_prices()