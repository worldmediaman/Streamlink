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

def extract_dai_url(content):
    # Regulärer Ausdruck, um die daiUrl von der neuen Seite zu extrahieren
    match = re.search(r"daiUrl\s*:\s*'(https://nowtv-live-ad\.ercdn\.net/nowtv/playlist\.m3u8\?st=[^']+)'", content)
    if match:
        return match.group(1)
    else:
        print("daiUrl not found in the content.")
        return None

def create_m3u8_content(dai_url):
    m3u8_content = [
        "#EXTM3U",
        "#EXTINF:-1, NOW",
        dai_url
    ]
    return "\n".join(m3u8_content)

def extract_urls_from_m3u8(content):
    # Extrahiere die URLs aus dem M3U8-Inhalt
    urls = re.findall(r'https://nowtv-live-ad\.ercdn\.net/nowtv/[^"]+', content)
    return urls

def main():
    global url  # Sicherstellen, dass die url-Variable global verfügbar ist
    site_content = fetch_website_content(url)
    if site_content:
        dai_url = extract_dai_url(site_content)
        if dai_url:
            m3u8_content = create_m3u8_content(dai_url)
            with open("output/02_now.m3u8", "w") as f:
                f.write(m3u8_content)
            print("Generated 02_now.m3u8 content:")
            print(m3u8_content)
            
            # Extrahiere die URLs aus der Datei und spiele sie ab (simuliert)
            urls = extract_urls_from_m3u8(m3u8_content)
            for url in urls:
                print(f"Playing URL: {url}")
                # Hier würdest du die URL tatsächlich abspielen (z.B. mit VLC oder einem anderen Player)

if __name__ == "__main__":
    main()
