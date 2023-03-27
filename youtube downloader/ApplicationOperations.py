import subprocess

class ApplicationOperations:
    def __init__(self) :
        pass

    # Execute a command
    def cmdexec(self,command):
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Command execution failed with error: {e}")
            return None

    # print a result or an error
    def error_handle(self,errormsg,result):
        if result:
            print({result})
        else:
            print(errormsg)


    def check_version(self):
        checkversioncommand = "yt-dlp --version"
        versionresult = self.cmdexec(checkversioncommand)
        if versionresult:
            print(f"yt-dlp version {versionresult}")
        else:
            print("Failed to get yt-dlp version")

    def update_app(self):        
        updateversioncommand = "yt-dlp -U"
        result = self.cmdexec(updateversioncommand)
        self.error_handle("Failed to update yt-dlp application",result)
        # if result:
        #     print({result})
        # else:
        #     print("Failed to update yt-dlp application")

    def view_formats(self,url):
        view_formats_command = f"yt-dlp -F {url}"
        result = self.cmdexec(view_formats_command)
        self.error_handle("Failed to view the formats of the video",result)
        # if result:
        #     print({result})
        # else:
        #     print("Failed to view the formats of the video")

    def download_single_video(self,url,quality):
        location = "F:\FireDM Downloads\%(title)s.mp4"
        if(quality=='best'):
            download_command = f"yt-dlp {url}"
        else:            
            download_command = f'yt-dlp -f "bestvideo[height<={quality}][ext=mp4]+bestaudio" -o "{location} {{}}{url}"'

        result = self.cmdexec(download_command)
        self.error_handle("Failed to download the video",result)
        # if result:
        #     print("Successfully downloaded!")
        #     # print({result})
        # else:
        #     print("Failed to download the video")

    def download_playlist(self,url):
        download_command = f"yt-dlp --yes-playlist {url}"
        result = self.cmdexec(download_command)
        self.error_handle("Failed to download the playlist",result)
        # if result:
        #     print({result})
        # else:
        #     print("Failed to download the playlist")

    def get_filename(self,url):
        command = f"yt-dlp --get-title {url}"
        filename = self.cmdexec(command)
        if filename:
            return filename
        else:
            print("Couldnt capture the filename")

    