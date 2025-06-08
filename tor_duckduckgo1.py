import requests

proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

url = 'https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/'

try:
    response = requests.get(url, proxies=proxies, timeout=10)
    print("✓ Success accessing DuckDuckGo Onion!")
    print(response.text[:1000])
except Exception as e:
    print("✗ Failed:", e)

