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
    # Aktualisiere den regulären Ausdruck, um die DAI-URL von der neuen Seite zu extrahieren
    match = re.search(r'(https://nowtv-live-ad\.ercdn\.net/nowtv/playlist\.m3u8\?st=[^\'"]+)', content)
    if match:
        return match.group(1)
    else:
        print("DAI URL not found in the content.")
        return None

def fetch_stream_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to fetch content.")
        return None

def modify_content(content):
    lines = content.split("\n")
    modified_content = ""
    for line in lines:
        if line.startswith("nowtv_"):
            modified_content += line + "\n"
        else:
            modified_content += line + "\n"
    return modified_content

def main():
    site_content = fetch_website_content(url)
    if site_content:
        dai_url = extract_dai_url(site_content)
        if dai_url:
            print("Extracted DAI URL:", dai_url)
            stream_content = fetch_stream_content(dai_url)
            if stream_content:
                modified_content = modify_content(stream_content)
                with open("output/02_now.m3u8", "w") as f:
                    f.write(modified_content)

if __name__ == "__main__":
    main()
