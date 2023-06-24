import subprocess

def execute_cmd(command:str,action:str):
    try:
        subprocess.check_call(command)
        success_msg = f"\n{action} completed successfully."
        print(success_msg)
    except subprocess.CalledProcessError as e:
        failed_msg = f"\n{action} failed with error: {e}"
        print(failed_msg)

def update():
    command = "yt-dlp -U"
    execute_cmd(command,"Update")

def version_check():
    command = "yt-dlp --version"
    execute_cmd(command,"Version check")

def download_video(height:int, url:str, folder_path="F:\FireDM Downloads"):
    command = [
        "yt-dlp",
        "-f", f"bestvideo[height<={height}][ext=mp4]+bestaudio",
        "-o", f"{folder_path}\%(title)s.mp4",
        url
    ]

    execute_cmd(command,"Download")

def download_best_video(url:str):
    command = f"yt-dlp {url}"
    execute_cmd(command,"download best video")