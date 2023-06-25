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

def download_video(height:str, url:str, folder_path="F:\FireDM Downloads"):
    command = [
        "yt-dlp",
        "-f", f"bestvideo[height<={height}][ext=mp4]+bestaudio",
        "-o", f"{folder_path}\%(title)s.mp4",
        url
    ]

    execute_cmd(command,"Download")

def download_best_video(url:str,folder_path ="F:\FireDM Downloads"):
    
    command = [
        "yt-dlp",
        "-f", f"bestvideo[ext=mp4]+bestaudio",
        "-o", f"{folder_path}\%(title)s.mp4",
        url
    ]
    execute_cmd(command,"Downloading best video")

def download_partial_playlist(url:str,height:str,start_index=1,end_index=None,folder_path ="F:\FireDM Downloads"):

    command = [
        'yt-dlp',
        url,
        '--playlist-start',
        str(start_index),
        '--playlist-end',
        str(end_index),
        '-f',
        f'bestvideo[height<={height}][ext=mp4]+bestaudio',
        '--merge-output-format',
        'mp4',
        '-o',
        f'{folder_path}/%(title)s.%(ext)s',
        '--continue'
    ]
    execute_cmd(command,"Downloading playlist")

def download_playlist(url, start_index, h, folder_path="F:\FireDM Downloads", end_index=None):
    command = [
        'yt-dlp',
        url,
        '--playlist-start',
        str(start_index),
    ]
    
    if end_index is not None:
        command.extend(['--playlist-end', str(end_index)])
        
    command.extend([
        '-f',
        f'bestvideo[height<={h}][ext=mp4]+bestaudio',
        '--merge-output-format',
        'mp4',
        '-o',
        f'{folder_path}/%(title)s.%(ext)s',
        '--continue'
    ])

    execute_cmd(command,"Downloading entire playlist")
