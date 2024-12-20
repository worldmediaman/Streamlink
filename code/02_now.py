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
    match = re.search(r'daionUrl\s*:\s*(mobilecheck\(\) == true \? \'(https://nowtv\.daioncdn\.net/nowtv/nowtv\.m3u8\?ce=3&app=mobile_web&st=[^\'"]+)\' : \'(https://nowtv\.daioncdn\.net/nowtv/nowtv\.m3u8\?ce=3&app=desktop_web&st=[^\'"]+)', content)
    if match:
        return match.group(2) if "mobile_web" in match.group(2) else match.group(3)
    else:
        print("daionURL not found in the content.")
        return None

def create_m3u8_content(daion_url):
    m3u8_content = [
        "#EXTM3U",
        "#EXT-X-VERSION:3",
        "#EXT-X-STREAM-INF:BANDWIDTH=1050000,AVERAGE-BANDWIDTH=950000,RESOLUTION=1280x720",
        f"{daion_url}",
        "#EXT-X-STREAM-INF:BANDWIDTH=800000,AVERAGE-BANDWIDTH=700000,RESOLUTION=854x480",
        f"{daion_url}",
        "#EXT-X-STREAM-INF:BANDWIDTH=550000,AVERAGE-BANDWIDTH=500000,RESOLUTION=640x360",
        f"{daion_url}"
    ]
    return "\n".join(m3u8_content)

def main():
    site_content = fetch_website_content(url)
    if site_content:
        daion_url = extract_daion_url(site_content)
        if daion_url:
            print(daion_url)  # Ausgabe der daionURL
            m3u8_content = create_m3u8_content(daion_url)
            with open("output/02_now.m3u8", "w") as f:
                f.write(m3u8_content)
            print(m3u8_content)

if __name__ == "__main__":
    main()
