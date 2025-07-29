import requests

def check_website_status(url):
    """Checks if a website is reachable and returns its status code."""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        print(f"Website {url} is reachable. Status code: {response.status_code}")
        return True
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Something went wrong: {err}")
    return False

if __name__ == "__main__":
    test_url = "https://www.google.com"
    check_website_status(test_url)
