import os

# Replace "C:\Example\Folder" with the path to the folder you want to navigate to
folder_path = r"F:\VS Code projects\python\youtube downloader"

# Change the current working directory to the specified folder
os.chdir(folder_path)

# Print the current working directory to verify that it has been changed
print("Current working directory:", os.getcwd())
