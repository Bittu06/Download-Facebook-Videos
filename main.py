import yt_dlp
import re

def sanitize_filename(filename, max_length=100):
    # Remove characters not allowed in filenames
    filename = re.sub(r'[\\/*?:"<>|]', "", filename)
    # Trim to max length
    return filename[:max_length]

def download_facebook_video(url, output_path="."):
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title).50B.%(ext)s',  # Limit title length to avoid OS errors
        'format': 'best',  # Best quality
        'restrictfilenames': True,  # Avoid weird characters in file names
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("✅ Download completed!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    fb_video_url = input("Enter Facebook video URL: ")
    download_facebook_video(fb_video_url, output_path="downloads")

        