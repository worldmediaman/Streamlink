def read_m3u8_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

def merge_m3u8_files(file_paths, output_path):
    merged_content = "#EXTM3U\n"
    for file_path in file_paths:
        content = read_m3u8_file(file_path)
        # Entferne die erste Zeile, wenn es sich um "#EXTM3U" handelt
        if content.startswith("#EXTM3U"):
            content = content.split('\n', 1)[1]
        merged_content += content + "\n"

    with open(output_path, "w") as output_file:
        output_file.write(merged_content)
    print(f"Merged content saved to '{output_path}'")

def main():
    file_paths = ["output/01_estar.m3u8", "output/02_now.m3u8"]
    output_path = "output/combined_playlist.m3u8"
    merge_m3u8_files(file_paths, output_path)

if __name__ == "__main__":
    main()
