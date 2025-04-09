import requests
import re

# کانال Twitch مورد نظر
channel = "ManotoArchive"

# گرفتن فایل m3u فعلی
with open("playlist.m3u", "r") as f:
    content = f.read()

# گرفتن لینک m3u جدید از سایت Twitch-proxy (یا مشابهش)
# این قسمت برای تست از streamlinkproxy استفاده می‌کنیم:
url = f"https://api.streamlinkproxy.com/{channel}.m3u8"
response = requests.get(url)

if response.status_code == 200:
    new_url = response.text.strip()
    print("New Twitch URL:", new_url)

    # جایگزین کردن URL در فایل m3u
    updated = re.sub(r'https://.*\.m3u8', new_url, content)

    # ذخیره
    with open("playlist.m3u", "w") as f:
        f.write(updated)
else:
    print("Failed to get new URL")
