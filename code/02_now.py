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

def create_m3u8_content(dai_url, resolution):
    if resolution == "best":
        resolution_tag = "#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=3000000,RESOLUTION=1920x1080"
        stream_url = dai_url.replace("playlist", "live_1080p3000000kbps/index")
    elif resolution == "1280":
        resolution_tag = "#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1500000,RESOLUTION=1280x720"
        stream_url = dai_url.replace("playlist", "live_720p1500000kbps/index")
    else:
        resolution_tag = "#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=3000000,RESOLUTION=1920x1080"
        stream_url = dai_url.replace("playlist", "live_1080p3000000kbps/index")

    m3u8_content = [
        "#EXTM3U",
        "#EXT-X-VERSION:3",
        resolution_tag,
        stream_url
    ]
    return "\n".join(m3u8_content)

def main():
    site_content = fetch_website_content(url)
    if site_content:
        dai_url = extract_dai_url(site_content)
        if dai_url:
            # Passe die gewünschte Auflösung hier an: "best" oder "1280"
            resolution = "best"
            m3u8_content = create_m3u8_content(dai_url, resolution)
            with open("output/02_now.m3u8", "w") as f:
                f.write(m3u8_content)
            print(m3u8_content)

if __name__ == "__main__":
    main()
