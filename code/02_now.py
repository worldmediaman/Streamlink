import requests
import re

# URL der Webseite, die den Live-Stream enthält
url = "https://www.nowtv.com.tr/canli-yayin"

def fetch_website_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to fetch the website content.")
        return None

def extract_daion_url(content):
    # Aktualisiere den regulären Ausdruck, um die daionURL von der neuen Seite zu extrahieren
    match = re.search(r'(https://nowtv\.daioncdn\.net/nowtv/nowtv\.m3u8\?ce=3&app=mobile_web&st=[^\'"]+)', content)
    if match:
        return match.group(1)
    else:
        print("daionURL not found in the content.")
        return None

def fetch_stream_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to fetch content.")
        return None

def create_m3u8_content(base_url):
    m3u8_content = [
        "#EXTM3U",
        "#EXT-X-VERSION:3",
        "#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=3000000,RESOLUTION=1920x1080",
        f"{base_url}nowtv_1080p.m3u8",
        "#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1500000,RESOLUTION=1280x720",
        f"{base_url}nowtv_720p.m3u8",
        "#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=900000,RESOLUTION=854x480",
        f"{base_url}nowtv_480p.m3u8"
    ]
    return "\n".join(m3u8_content)

def main():
    site_content = fetch_website_content(url)
    if site_content:
        daion_url = extract_daion_url(site_content)
        if daion_url:
            print(daion_url)  # Ausgabe der daionURL
            base_url = re.match(r'(https://nowtv\.daioncdn\.net/nowtv/)', daion_url).group(1)
            m3u8_content = create_m3u8_content(base_url)
            with open("output/02_now.m3u8", "w") as f:
                f.write(m3u8_content)
            print(m3u8_content)

if __name__ == "__main__":
    main()
