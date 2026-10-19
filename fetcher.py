from config import USER_AGENT, TIMEOUT_SECONDS, RAW_DIR, MAX_RETRIES, DELAY_SECONDS
import requests
import re
import os
from pathlib import Path
from time import sleep
import logging



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

def fetch_with_cache(url):
    path = name_file_cache(url)
    if Path(path).is_file():
        return Path(path).read_text(encoding="utf-8")

    Path(RAW_DIR).mkdir(parents=True, exist_ok=True)

    attempt = 1
    while attempt <= MAX_RETRIES:
        try:
            html = fetch_url(url)
            Path(path).write_text(html, encoding="utf-8")
            sleep(DELAY_SECONDS)

            return html

        except RuntimeError:
            logging.warning(f"Failed to fetch {url} (attempt {attempt})")
            sleep(DELAY_SECONDS * attempt * 2)
            attempt = attempt + 1

        raise requests.RequestException(f"Failed to fetch {url} after {MAX_RETRIES} attempts")
        