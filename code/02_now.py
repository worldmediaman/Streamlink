import time

# Feste Parameter (ersetzt durch funktionierende Beispiele)
st_token = "5g0ZFPxzUckSxxPRbtc8fw"
expiry_time = int(time.time()) + 3600  # Ablaufzeit in 1 Stunde (in der Zukunft)

base_url = "https://nowtv-live-ad.ercdn.net/nowtv/"
query_params = f"st={st_token}&e={expiry_time}"

m3u8_content = [
    "#EXTM3U",
    "#EXT-X-VERSION:3",
    "#EXT-X-INDEPENDENT-SEGMENTS",
    "#EXT-X-STREAM-INF:PROGRAM-ID=2850,AVERAGE-BANDWIDTH=950000,BANDWIDTH=1050000,NAME=720p,RESOLUTION=1280x720",
    f"{base_url}nowtv_720p.m3u8?{query_params}",
    "#EXT-X-STREAM-INF:PROGRAM-ID=2850,AVERAGE-BANDWIDTH=700000,BANDWIDTH=800000,NAME=480p,RESOLUTION=854x480",
    f"{base_url}nowtv_480p.m3u8?{query_params}",
    "#EXT-X-STREAM-INF:PROGRAM-ID=2850,AVERAGE-BANDWIDTH=500000,BANDWIDTH=550000,NAME=360p,RESOLUTION=640x360",
    f"{base_url}nowtv_360p.m3u8?{query_params}"
]

# Schreiben in eine Datei
with open("output/02_now.m3u8", "w") as f:
    f.write("\n".join(m3u8_content))

print("\n".join(m3u8_content))
