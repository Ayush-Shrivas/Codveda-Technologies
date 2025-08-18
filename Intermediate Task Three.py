import requests

def get_crypto_price(coin="bitcoin", currency="usd"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        price = data[coin][currency]
        print(f"💰 Current {coin.capitalize()} price: {price} {currency.upper()}")

    except requests.exceptions.RequestException as e:
        print("❌ Error fetching data:", e)
    except KeyError:
        print("⚠️ Unexpected response format!")

# Example usage
get_crypto_price("ethereum", "usd")
