import subprocess
import re

# فایل M3U اصلی
M3U_FILE = "playlist.m3u"

# کانالی که می‌خوای لینک M3U8ش آپدیت بشه
channel_name = "ManotoArchive"

def get_stream_url(channel):
    try:
        result = subprocess.run(
            ["streamlink", f"https://twitch.tv/{channel}", "best", "--stream-url"],
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

    # لینک قبلی رو با جدید جایگزین کن (اگر برچسب خاصی داشته باشه بهتره)
    updated_content = re.sub(
        r"https?://.*?ManotoArchive.*?\.m3u8",
        new_url,
        content
    )

    with open(M3U_FILE, "w", encoding="utf-8") as file:
        file.write(updated_content)

if __name__ == "__main__":
    stream_url = get_stream_url(channel_name)
    if stream_url:
        print(f"Got stream URL: {stream_url}")
        update_m3u_file(stream_url)
    else:
        print("Failed to get stream URL.")
