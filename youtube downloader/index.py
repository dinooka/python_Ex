import os
import subprocess
from ApplicationOperations import ApplicationOperations

#  create an object for operations class
operations = ApplicationOperations() 

print('***********************************************************')
print('\t\tYoutube downloader\t')
print('***********************************************************')

nwd = os.chdir('F:\Youtube - dl');
# print("present working directory : {0}".format(os.getcwd()))



# Main menu
print("\nSelect the below options")
print("\n1. Download a video")
print("2. Download a playlist")
print("3. Check the version")
print("4. Update the Application")
print("5. Close the Application")

main_menu_option = input("\nSelect an option from above list(Type the number): ")

if(main_menu_option == '3'):
    operations.check_version() 

elif(main_menu_option == '4'):
    operations.update_app()

elif(main_menu_option == '1'):
    url = input("Enter the url: ")
    # print("Enter the download location(Type 'd' for default location, else give the folder path...)")
    # location = input("Download location: ")
    print("\n1. Select the quality of the video")
    print("2. Download the best audio/video quality video")
    download_option = input("Select the above options: ")
    if(download_option=='1'):
        quality = input("Enter the frame height: ")
        operations.download_single_video(url,quality)
    else:
        operations.download_single_video(url,'best')  

elif(main_menu_option == '2'):
    operations.download_playlist()

elif(main_menu_option == '5'):
    # operations.update_app()      
    print("function not defined!")


# viewavailableformats = f"yt-dlp -F {url}"

# viewformats = cmdexec(viewavailableformats)
# if viewformats:
#     print(f"Formats: {viewformats}")
# else:
#     print("Failed to get available formats")


