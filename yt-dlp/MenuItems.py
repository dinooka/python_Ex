import operations as op

def dwnld_video_options():
    url = input("Enter the url: ")
    print("Enter the download location(Type 'd' for default location, else give the folder path...)")
    location = input("Download location: ")
    print("\na. Select the quality of the video")
    print("b. Download the best audio/video quality video")
    download_option = input("Select the above options: ")
    
    if(download_option=='a'):
        quality = input("Enter the frame height: ")
        if(location == ''):
            op.download_video(quality,url)
        else:            
            op.download_video(quality,url,location)       
    else:
        op.download_best_video(url) 

def main_menu():
        
    print('\n***********************************************************')
    print('\t\tYoutube downloader\t')
    print('***********************************************************')

    # Main menu
    print("\nSelect the below options")
    print("\n1. Download a video")
    print("2. Download a playlist")
    print("3. Check the version")
    print("4. Update the Application")
    print("5. Close the Application")

    menuoption = input("\nSelect an option from above list(Type the number): ")
    return menuoption