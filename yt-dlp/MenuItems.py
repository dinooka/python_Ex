import operations as op

def dwnld_video_options():
    url = input("Enter the url: ")
    print("\nEnter the download location(Press 'Enter' for default location, else give the folder path...)")
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
    elif((download_option == 'b')):
        if(location == ''):
            op.download_best_video(url)
        else:            
            op.download_best_video(url,location)

def dwnld_playlist_options():
    url = input("Enter the url: ")
    print("\nEnter the download location(Press 'Enter' for default location, else give the folder path...)")
    location = input("Download location: ")
    resolution = input("Enter the video resolution: ")
    print("a. Download an entire playlist")
    print("b. Download a partial playlist")
    download_option = input("Select the above options: ")
    
    if(download_option=='a'):
        if(location == ''):                        
            op.download_playlist(url,1,resolution)
        else:                      
            op.download_playlist(url,1,resolution,location)
    elif((download_option == 'b')):
        start_index = input("Enter the start index: ")
        end_index = input("Enter the end index: ")
        if(location == ''):
            op.download_partial_playlist(url,resolution,start_index,end_index)
        else:            
            op.download_partial_playlist(url,resolution,start_index,end_index,location)
        

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

    return input("\nSelect an option from above list(Type the number): ")