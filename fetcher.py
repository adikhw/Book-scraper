import requests
from config import USER_AGENT, TIMEOUT_SECONDS

def fetch_url(url):
    response = requests.get(
        url, 
        headers={"User-Agent": USER_AGENT}, 
        timeout=TIMEOUT_SECONDS,
        )
    response.raise_for_status()
    
    response.encoding = "utf-8"
    return response.text