from pytube import YouTube

def Downloader(link):
    url =YouTube(str(link))
    video = url.streams.first()
    video.download()

Downloader(r"https://www.youtube.com/watch?v=3EOcHuerjJA&feature=youtu.be")
