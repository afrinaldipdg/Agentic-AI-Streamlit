import requests

def search_duckduckgo_tor(query):
    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
                      'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                      'Chrome/114.0.0.0 Safari/537.36'
    }
    url = "https://html.duckduckgo.com/html/"
    params = {'q': query}
    
    try:
        r = requests.get(url, params=params, proxies=proxies, headers=headers, timeout=20)
        r.raise_for_status()
        return r.text
    except requests.RequestException as e:
        return f"Request failed: {e}"

if __name__ == "__main__":
    html = search_duckduckgo_tor("What's the capital of Norway?")
    print(html[:1000])  # print potongan hasil html

