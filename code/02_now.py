import time

# Feste Parameter (ersetzt durch funktionierende Beispiele)
st_token = "FH49muhyqgfVctbYiVpaQw"
expiry_time = 1734735955  # Setze den Ablaufzeitpunkt auf den gleichen Wert wie die Webseite

base_url = "https://nowtv-live-ad.ercdn.net/nowtv/"
query_params = f"st={st_token}&e={expiry_time}"

m3u8_content = [
    "#EXTM3U",
    "#EXT-X-VERSION:3",
    "#EXT-X-INDEPENDENT-SEGMENTS",
    "#EXT-X-STREAM-INF:PROGRAM-ID=2850,AVERAGE-BANDWIDTH=950000,BANDWIDTH=1050000,NAME=720p,RESOLUTION=1280x720",
    f"{base_url}playlist.m3u8?{query_params}",
    "#EXT-X-STREAM-INF:PROGRAM-ID=2850,AVERAGE-BANDWIDTH=700000,BANDWIDTH=800000,NAME=480p,RESOLUTION=854x480",
    f"{base_url}playlist.m3u8?{query_params}",
    "#EXT-X-STREAM-INF:PROGRAM-ID=2850,AVERAGE-BANDWIDTH=500000,BANDWIDTH=550000,NAME=360p,RESOLUTION=640x360",
    f"{base_url}playlist.m3u8?{query_params}"
]

# Schreiben in eine Datei
with open("output/02_now.m3u8", "w") as f:
    f.write("\n".join(m3u8_content))

print("\n".join(m3u8_content))
