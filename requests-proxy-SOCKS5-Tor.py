import requests

def duckduckgo_search_via_tor(query):
    proxies = {
        'http':  'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    url = 'https://html.duckduckgo.com/html/'
    params = {'q': query}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
                      'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                      'Chrome/114.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(url, params=params, proxies=proxies, headers=headers, timeout=30)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return f"Request failed: {e}"

if __name__ == "__main__":
    query = "What's the capital of Norway?"
    result_html = duckduckgo_search_via_tor(query)
    print(result_html)

