import pytube

def Download(link):
    yt=pytube.YouTube(link)
    yt=yt.streams.get_highest_resolution()
    try:
        yt.download("C:/Users/shrey/Dropbox/PC/Downloads")
    except:
        print("an error has occured")
    print("Download is completed")
link=input("Enter Youtube video URL: ")
Download(link)
