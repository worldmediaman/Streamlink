import requests

# URLs der Dateien auf GitHub
urls = [
    "https://raw.githubusercontent.com/worldmediaman/Streamlink/refs/heads/main/output/01_estar.m3u8",
    "https://raw.githubusercontent.com/worldmediaman/Streamlink/refs/heads/main/output/02_now.m3u8"
]

def fetch_file_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch the file content from {url}.")
        return None

def read_m3u8_file(content):
    return content

def merge_m3u8_files(urls, output_path):
    merged_content = "#EXTM3U\n#EXT-X-VERSION:3\n"
    for url in urls:
        content = fetch_file_content(url)
        if content:
            # Prüfen, ob #EXTINF:-1, STAR oder #EXTINF:-1, NOW vorhanden sind
            lines = content.split("\n")
            if "#EXTINF:-1, STAR" in content:
                content = "\n".join([line for line in lines if not line.startswith("#EXTM3U")])
            elif "#EXTINF:-1, NOW" in content:
                content = "\n".join([line for line in lines if not line.startswith("#EXTM3U")])
            merged_content += content + "\n"

    with open(output_path, "w") as output_file:
        output_file.write(merged_content)
    print(f"Merged content saved to '{output_path}'")

def main():
    output_path = "output/combined_playlist.m3u8"
    merge_m3u8_files(urls, output_path)

if __name__ == "__main__":
    main()
