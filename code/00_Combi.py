# Direktes Beispiel der funktionierenden URL
url_720p = "https://nowtv-live-ad.ercdn.net/nowtv/nowtv_720p.m3u8?e=1734781560&st=h-xrRokfmtw4t7J7tEc-zg"
url_480p = "https://nowtv-live-ad.ercdn.net/nowtv/nowtv_480p.m3u8?e=1734781560&st=h-xrRokfmtw4t7J7tEc-zg"
url_360p = "https://nowtv-live-ad.ercdn.net/nowtv/nowtv_360p.m3u8?e=1734781560&st=h-xrRokfmtw4t7J7tEc-zg"

# Erstellen der M3U8-Datei
m3u8_content = [
    "#EXTM3U",
    "#EXT-X-VERSION:3",
    "#EXT-X-INDEPENDENT-SEGMENTS",
    "#EXT-X-STREAM-INF:PROGRAM-ID=2850,AVERAGE-BANDWIDTH=950000,BANDWIDTH=1050000,NAME=720p,RESOLUTION=1280x720",
    url_720p,
    "#EXT-X-STREAM-INF:PROGRAM-ID=2850,AVERAGE-BANDWIDTH=700000,BANDWIDTH=800000,NAME=480p,RESOLUTION=854x480",
    url_480p,
    "#EXT-X-STREAM-INF:PROGRAM-ID=2850,AVERAGE-BANDWIDTH=500000,BANDWIDTH=550000,NAME=360p,RESOLUTION=640x360",
    url_360p
]

# Schreiben in eine Datei
with open("output/02_now_fixed.m3u8", "w") as f:
    f.write("\n".join(m3u8_content))

print("\n".join(m3u8_content))
