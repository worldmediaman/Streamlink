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
    m3u8_content = [
        "#EXTM3U",
        "#EXT-X-VERSION:3",
        "#EXT-X-STREAM-INF:BANDWIDTH=1050000,AVERAGE-BANDWIDTH=950000,RESOLUTION=1280x720",
        dai_url,
        "#EXT-X-STREAM-INF:BANDWIDTH=800000,AVERAGE-BANDWIDTH=700000,RESOLUTION=854x480",
        dai_url,
        "#EXT-X-STREAM-INF:BANDWIDTH=550000,AVERAGE-BANDWIDTH=500000,RESOLUTION=640x360",
        dai_url
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
