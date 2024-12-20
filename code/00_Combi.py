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

def main():
    site_content = fetch_website_content(url)
    if site_content:
        dai_url = extract_dai_url(site_content)
        if dai_url:
            m3u8_content = create_m3u8_content(dai_url)
            with open("output/02_now.m3u8", "w") as f:
                f.write(m3u8_content)
            print(m3u8_content)

            # Erstellen einer zusammengeführten Playliste
            combined_content = [
                "#EXTM3U",
                "#EXTINF:-1, TEST 1",
                "https://raw.githubusercontent.com/worldmediaman/Streamlink/refs/heads/main/output/01_estar.m3u8",
                "#EXTINF:-1, TEST 2",
                "https://raw.githubusercontent.com/worldmediaman/Streamlink/refs/heads/main/output/02_now.m3u8"
            ]

            with open("output/combined_playlist.m3u8", "w") as f_combined:
                f_combined.write("\n".join(combined_content))
            print("Combined playlist created: output/combined_playlist.m3u8")

if __name__ == "__main__":
    main()
