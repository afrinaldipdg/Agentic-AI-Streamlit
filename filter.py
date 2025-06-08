import requests
try:
    response = requests.get("https://www.google.com", timeout=10)
    response.raise_for_status()
    print("Google.com accessed successfully.")
except requests.RequestException as e:
    print(f"Failed to access Google.com: {e}")
