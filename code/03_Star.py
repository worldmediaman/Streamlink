import subprocess
import sys

# Sicherstellen, dass beautifulsoup4 installiert ist
try:
    from bs4 import BeautifulSoup
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "beautifulsoup4"])
    from bs4 import BeautifulSoup

import requests
import re

url = "https://www.startv.com.tr/canli-izle"

def fetch_website_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("Website content fetched successfully.")
        return response.text
    else:
        print("Failed to fetch the website content.")
        return None

def extract_live_url(content):
    print("Extracting live URL from content...")
    soup = BeautifulSoup(content, "html.parser")
    script_tags = soup.find_all("script")
    for script in script_tags:
        if "liveUrl" in script.string:
            match = re.search(r'liveUrl = \'(.*?)\'', script.string)
            if match:
                print("Live URL found:", match.group(1))
                return match.group(1)
    print("Live URL not found in the content.")
    return None

def fetch_stream_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("Stream content fetched successfully.")
        return response.text
    else:
        print("Failed to fetch content.")
        return None

def modify_content(content, base_url):
    print("Modifying stream content...")
    lines = content.split("\n")
    modified_content = ""
    for line in lines:
        if line.startswith("live_"):
            full_url = base_url + line
            modified_content += full_url + "\n"
        else:
            modified_content += line + "\n"
    return modified_content

def main():
    site_content = fetch_website_content(url)
    if site_content:
        live_url = extract_live_url(site_content)
        if live_url:
            stream_content = fetch_stream_content(live_url)
            if stream_content:
                base_url = "https://mn-nl.mncdn.com/dogusdyg_star/"
                modified_content = modify_content(stream_content, base_url)
                print("Modified Content:")
                print(modified_content)

if __name__ == "__main__":
    main()
