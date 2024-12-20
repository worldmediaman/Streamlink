import requests
import re

# URL der Datei auf GitHub
url = "https://raw.githubusercontent.com/worldmediaman/Streamlink/main/output/02_now.m3u8"

def fetch_file_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to fetch the file content.")
        return None

def main():
    file_content = fetch_file_content(url)
    if file_content:
        print(file_content)

if __name__ == "__main__":
    main()
