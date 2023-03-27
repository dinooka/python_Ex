import argparse
import yt_dlp

parser = argparse.ArgumentParser(description='Download a YouTube video with a specific height')
parser.add_argument('url', type=str, help='The URL of the YouTube video to download')
parser.add_argument('hval', type=int, help='The maximum height of the video to download')
args = parser.parse_args()

ydl_opts = {
    'format': f'bestvideo[height<={args.hval}][ext=mp4]+bestaudio',
    'outtmpl': r'F:\FireDM Downloads\%(title)s.mp4'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([args.url])
