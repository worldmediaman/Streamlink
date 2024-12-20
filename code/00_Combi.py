import requests

# URL der Datei auf GitHub
url = "https://raw.githubusercontent.com/worldmediaman/Streamlink/main/output/02_now.m3u8"

def fetch_file_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Überprüft, ob die Anfrage erfolgreich war
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch the file content: {e}")
        return None

def main():
    file_content = fetch_file_content(url)
    if file_content:
        # Direkt den Inhalt ausgeben
        print("Fetched File Content:")
        print(file_content)
        
        # Speichern in einer Datei
        with open("output/fetched_now.m3u8", "w") as f:
            f.write(file_content)
        print("\nFetched content saved to 'output/fetched_now.m3u8'")
    else:
        print("No content fetched.")

if __name__ == "__main__":
    main()
