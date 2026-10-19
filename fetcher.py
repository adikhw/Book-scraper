from config import USER_AGENT, TIMEOUT_SECONDS, RAW_DIR
import requests
import re
import os

def fetch_url(url):
    response = requests.get(
        url, 
        headers={"User-Agent": USER_AGENT}, 
        timeout=TIMEOUT_SECONDS,
        )
    response.raise_for_status()
    
    response.encoding = "utf-8"
    return response.text

def name_file_cache(url):
    clean_url = re.sub(r'https?://(www\.)?', '', url)
    name_file = re.sub(r'[^a-zA-Z0-9]', '_', clean_url)
    name_file = re.sub(r'_+', '_', name_file).strip('_')

    complete_file_name = name_file + ".html"

    return os.path.join(RAW_DIR, complete_file_name)