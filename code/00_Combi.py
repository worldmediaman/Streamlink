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
    params = dai_url.split('?')[1]
    params_dict = dict(param.split('=') for param in params.split('&'))
    
    # Ablaufzeit berechnen
    expiry_time = int(time.time()) + 3600  # Ablaufzeit in 1 Stunde
    params_dict['e'] = str(expiry_time)
    
    # Reihenfolge der Parameter sicherstellen
    query_params = f"e={params_dict['e']}&st={params_dict['st']}"
    
    m3u8_content = [
        "#EXTM3U",
        "#EXT-X-VERSION:3",
        "#EXT-X-INDEPENDENT-SEGMENTS",
        "#EXT-X-STREAM-INF:PROGRAM-ID=2850,AVERAGE-BANDWIDTH=950000,BANDWIDTH=1050000,NAME=720p,RESOLUTION=1280x720",
        f"{base_url}nowtv_720p.m3u8?{query_params}",
        "#EXT-X-STREAM-INF:PROGRAM-ID=2850,AVERAGE-BANDWIDTH=700000,BANDWIDTH=800000,NAME=480p,RESOLUTION=854x480",
        f"{base_url}nowtv_480p.m3u8?{query_params}",
        "#EXT-X-STREAM-INF:PROGRAM-ID=2850,AVERAGE-BANDWIDTH=500000,BANDWIDTH=550000,NAME=360p,RESOLUTION=640x360",
        f"{base_url}nowtv_360p.m3u8?{query_params}"
    ]
    return "\n".join(m3u8_content)

def main():
    site_content = fetch_website_content(url)
    if site_content:
        dai_url = extract_dai_url(site_content)
        if dai_url:
            m3u8_content = create_m3u8_content(dai_url)
            with open("output/02_now.m3u8", "w") as f:
                f.write(m3u8_content)
            print(m3u8_content)

if __name__ == "__main__":
    main()
