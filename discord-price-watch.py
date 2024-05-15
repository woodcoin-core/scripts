import json
import requests


COIN_NAME = "Woodcoin (LOG)"
COIN_HEADER = "Woodcoin"
COIN_PRICE_NAME = "woodcoin"
COIN_GECKO = "https://www.coingecko.com/en/coins/woodcoin"
COIN_AVATAR = "https://raw.githubusercontent.com/woodcoin-core/media/main/logo/woodcoin128x128.png"
WEBHOOK = ""
DISCORD_COIN_COLOR = 4769149


if __name__ == '__main__':
    try:
        price_url = "https://api.coingecko.com/api/v3/coins/woodcoin"
        price = requests.request("GET", price_url).json()
    except requests.exceptions.HTTPError:
        print("HTTPError")
    except requests.exceptions.Timeout:
        print("Timeout")
    except requests.exceptions.TooManyRedirects:
        print("TooManyRedirects")
    except requests.exceptions.RequestException:
        print("RequestException")
    else:
        current_price_raw = price['market_data']['current_price']['sats'] * (10**-8)
        current_price = f"{current_price_raw:0.8f}"
        ath_raw = price['market_data']['ath']['sats'] * (10**-8)
        ath = f"{ath_raw:0.8f}"
        more_info = "(" + COIN_GECKO + ")"

        data = {"content": "",
                "username": COIN_HEADER + " Price Updates",
                "avatar_url": COIN_AVATAR,
                "type": "rich",
                "embeds": [
                    {
                        "title": "Current Price",
                        "color": DISCORD_COIN_COLOR,
                        "author": {
                            "name": COIN_NAME,
                            "icon_url": COIN_AVATAR
                        },
                        "image": {},
                        "thumbnail": {},
                        "footer": {
                            "text": "Price is shown in BTC.",
                            "type": "rich"
                        },
                        "fields": [
                            {
                                "name": "Coin Price",
                                "value": f'Current: {current_price}\nATH: {ath}',
                                "inline": "true"
                            },
                            {
                                "name": "More Info",
                                "value": "[@ CoinGecko]" + more_info,
                                "inline": "true"
                            }
                        ]
                    }
                ]}
        requests.post(WEBHOOK, json=data)
