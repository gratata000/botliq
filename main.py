import cloudscraper
import random
import time
import json

# Token Authorization
headers = {
    "Authorization": "Bearer YOUR_TOKEN_HERE",
    "Content-Type": "application/json"
}

scraper = cloudscraper.create_scraper()

def get_usd_balance():
    url = "https://api.testnet.liqfinity.com/v1/user/wallets"
    try:
        response = scraper.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            usdtotal = data['data']['summary']['usdBalance']
            usdsavl = data['data']['summary']['usdAvailableCredit']
            usd_balance_str = str(int(usdtotal - usdsavl))
            return usd_balance_str  # Mengembalikan string yang berisi bilangan bulat
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None
    except (json.JSONDecodeError, KeyError) as e:
        print(f"JSON Parsing Error: {str(e)}")
        return None

def log_activity(message):
    with open("activity_log.txt", "a") as log_file:
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")
    print(message)

if __name__ == "__main__":
    usd_balance = get_usd_balance()
    if usd_balance is not None:
        print(f"USDT Tersedia: {usd_balance}")
        amount = int(usd_balance)  # Konversi ke integer jika diperlukan untuk perhitungan
    else:
        amount = 0

    cycle_count = 0

    while True:
        try:
            cycle_count += 1
            log_activity(f"=== Siklus ke-{cycle_count} dimulai ===")
            # Implement your lock-unlock logic here
            time.sleep(random.uniform(30, 60))  # Placeholder delay
        except KeyboardInterrupt:
            log_activity("Proses dihentikan oleh pengguna.")
            break
        except Exception as e:
            log_activity(f"Terjadi kesalahan: {str(e)}")
