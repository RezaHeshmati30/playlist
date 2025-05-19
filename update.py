import subprocess
import re

M3U_FILE = "playlist.m3u"

# فقط آیدی ویدیو رو بذار، نه کل لینک
youtube_video_id = "QeiFiF9VTtw"  # از لینک استخراج شده

def get_youtube_stream_url(video_id):
    try:
        result = subprocess.run(
            ["streamlink", f"https://www.youtube.com/watch?v={video_id}", "best", "--stream-url"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        url = result.stdout.strip()
        if url.startswith("http"):
            return url
    except Exception as e:
        print("Error while fetching stream URL:", e)
    return None

def update_m3u_file(new_url):
    with open(M3U_FILE, "r", encoding="utf-8") as file:
        content = file.read()

    # فرض بر اینکه قبلاً در m3u یک خط با برچسب خاص برای یوتیوب گذاشتی
    updated_content = re.sub(
        r"https?://.*?youtube.*?\.m3u8",
        new_url,
        content
    )

    with open(M3U_FILE, "w", encoding="utf-8") as file:
        file.write(updated_content)

if __name__ == "__main__":
    stream_url = get_youtube_stream_url(youtube_video_id)
    if stream_url:
        print(f"Got stream URL: {stream_url}")
        update_m3u_file(stream_url)
    else:
        print("Failed to get stream URL.")