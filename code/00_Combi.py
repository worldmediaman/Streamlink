import requests

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
        print("Fetched File Content:")
        print(file_content)
        
        # Erstellen einer M3U-Playliste
        m3u_content = [
            "#EXTM3U",
            "#EXTINF:-1, NOW",
            "https://nowtv-live-ad.ercdn.net/nowtv/playlist.m3u8?st=S7qnLqUNsLx9v4BUkeYl4w&e=1734738360"
        ]
        
        # Schreiben in eine Datei
        with open("output/combined_playlist_direct.m3u8", "w") as f:
            f.write("\n".join(m3u_content))
        
        print("\nCreated M3U Playlist:")
        print("\n".join(m3u_content))

if __name__ == "__main__":
    main()
