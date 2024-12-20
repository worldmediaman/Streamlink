import requests
import re
import time

# URL der Webseite, die den Live-Stream enthält
url = "https://www.nowtv.com.tr/canli-yayin"

def fetch_website_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to fetch the website content.")
        return None

def extract_dai_url(content):
    # Regulärer Ausdruck, um die daiUrl von der neuen Seite zu extrahieren
    match = re.search(r"daiUrl\s*:\s*'(https://nowtv-live-ad\.ercdn\.net/nowtv/playlist\.m3u8\?st=[^']+)'", content)
    if match:
        return match.group(1)
    else:
        print("daiUrl not found in the content.")
        return None

def create_m3u8_content(dai_url):
    # Parameter extrahieren
    base_url = "https://nowtv-live-ad.ercdn.net/nowtv/"
    query_params = dai_url.split('?')[1]
    
    # Ablaufzeit berechnen
    expiry_time = int(time.time()) + 3600  # Ablaufzeit in 1 Stunde
    query_params = f"{query_params}&e={expiry_time}"
    
    m3u8_content = 
