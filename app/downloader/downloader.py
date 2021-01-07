from __future__ import unicode_literals
import os
from pathlib import Path
import youtube_dl

class Downloader:
    def __init__(self):

        resource_directory = Path(
            __file__).resolve().parents[2].joinpath("resources")

        self.download_directory = resource_directory.joinpath("sounds")
        self.current_id = self.calculateSoundFile()

    def calculateSoundFile(self):
        count = 0
        for temp_file in os.listdir(self.getDownloadDirectory()):
            if (temp_file.endswith(".mp3")):
                count+=1
        return count

    def download(self, name, link):
        self.current_id += 1
        downloadPath = str(
            self.download_directory.joinpath(f"{self.current_id}_{name}.%(ext)s"))
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': downloadPath
        }
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
        except:
            print("Failed to download file. Please check your link..")
            
    def getDownloadDirectory(self):
        return str(self.download_directory)
