import requests
import re

url = "https://www.nowtv.com.tr/canli-yayin"

def fetch_website_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to fetch the website content.")
        return None

def extract_dai_url(content):
    match = re.search(r"daiUrl\s*:\s*'(https://nowtv-live-ad\.ercdn\.net/nowtv/playlist\.m3u8\?st=[^']+)'", content)
    if match:
        return match.group(1)
    else:
        print("daiUrl not found in the content.")
        return None

def create_m3u8_content(dai_url):
    base_url = dai_url.split('?')[0]
    query_params = dai_url.split('?')[1]
    m3u8_content = [
        "#EXTM3U",
        "#EXT-X-VERSION:3",
        "#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=3000000,RESOLUTION=1920x1080",
        f"{base_url}/live_1080p3000000kbps/index.m3u8?{query_params}",
        "#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1500000,RESOLUTION=1280x720",
        f"{base_url}/live_720p1500000kbps/index.m3u8?{query_params}",
        "#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=900000,RESOLUTION=854x480",
        f"{base_url}/live_480p900000kbps/index.m3u8?{query_params}"
    ]
    return "\n".join(m3u8_content)

def main():
    site_content = fetch_website_content(url)
    if site_content:
        dai_url = extract_dai_url(site_content)
        if dai_url:
            m3u8_content = create_m3u8_content(dai_url)
            with open("output/now.m3u8", "w") as f:
                f.write(m3u8_content)
            print(m3u8_content)

if __name__ == "__main__":
    main()
