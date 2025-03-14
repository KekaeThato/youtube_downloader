
from yt_dlp import YoutubeDL
from pathlib import Path
import shutil,os

path_to_save = "./Youtube-Downloader"
path_to_current = os.path.dirname(os.path.realpath(__file__))

def download(url:str, path: str):

    with YoutubeDL() as ytd:
        ytd.download(url)
        test =ytd.extract_info(url)
        if test['title'].endswith(".mp4"):
            name = test['title']+".mp4"
            print("name:",name)
            save_to_file(name, path)

def check_and_or_create_path(path_to_analysis: str)->str:
    """This function check if given path exists if it doesn't it creates it
    """
    output_folder = Path(path_to_analysis)

    if not output_folder.exists():
        output_folder.mkdir(parents=True, exist_ok=True)
    return output_folder

def save_to_file(source: str, destination)->None:
    """"""
    check_and_or_create_path(destination)
    shutil.move(source, destination)


def main():
    url = input("Enter the link of the video you want to downlaod: ")
    if "https" not in url:
        raise ValueError("please insert a correct url link")
    
    
    try:
        print("downloading video...")
        download(url, path_to_save)
        print("download complete")
        print("url saved to history")
    except ValueError:
        print("Something went wrong, please try again")

if __name__ == "__main__":
    main()