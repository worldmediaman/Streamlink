combined_content = [
    "#EXTM3U",
    "#EXTINF:-1, TEST 1",
    "https://nowtv-live-ad.ercdn.net/nowtv/playlist.m3u8?st=S7qnLqUNsLx9v4BUkeYl4w&e=1734738360",
    "#EXTINF:-1, TEST 2",
    "https://raw.githubusercontent.com/worldmediaman/Streamlink/refs/heads/main/output/02_now.m3u8"
]

# Schreiben in eine Datei
with open("output/combined_playlist_direct.m3u8", "w") as f:
    f.write("\n".join(combined_content))

print("Direct combined playlist created: output/combined_playlist_direct.m3u8")
