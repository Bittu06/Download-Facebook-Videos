import youtube_dl

def download_facebook_video(video_url):
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',  # Output file template
        # Additional options can be added here as needed
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([video_url])
            print("Download completed successfully!")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    # Take the URL as input from the user
    video_url = input("Enter the Facebook video URL: ").strip()
    if video_url:
        download_facebook_video(video_url)
    else:
        print("No URL provided. Exiting.")