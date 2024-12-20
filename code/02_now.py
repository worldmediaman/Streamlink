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

def extract_live_url(content):
    match = re.search(r"daionUrl\s*:\s*'(https://nowtv\.daioncdn\.net/nowtv/nowtv\.m3u8\?ce=3&app=[^']+)'", content)
    if match:
        return match.group(1)
    else:
        print("Live URL not found in the content.")
        return None

def create_m3u8_content(live_url):
    # URLs für verschiedene Auflösungen definieren
    m3u8_content = [
        "#EXTM3U",
        "#EXT-X-VERSION:3",
        "#EXT-X-STREAM-INF:BANDWIDTH=1050000,AVERAGE-BANDWIDTH=950000,RESOLUTION=1280x720",
        f"{live_url}",
        "#EXT-X-STREAM-INF:BANDWIDTH=800000,AVERAGE-BANDWIDTH=700000,RESOLUTION=854x480",
        f"{live_url}",
        "#EXT-X-STREAM-INF:BANDWIDTH=550000,AVERAGE-BANDWIDTH=500000,RESOLUTION=640x360",
        f"{live_url}"
    ]
    return "\n".join(m3u8_content)

def main():
    site_content = fetch_website_content(url)
    if site_content:
        live_url = extract_live_url(site_content)
        if live_url:
            print(live_url)  # Ausgabe der Live-URL zur Überprüfung
            m3u8_content = create_m3u8_content(live_url)
            with open("output/02_now.m3u8", "w") as f:
                f.write(m3u8_content)
            print(m3u8_content)

if __name__ == "__main__":
    main()
