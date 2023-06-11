import os
from pytube import YouTube

class Youtube:
    def video_downloader(self, link):
        yt = YouTube(link)
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path=".")
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)


y=Youtube()
link=input("Enter youtube Video link :")
y.video_downloader(link)

import pkg_resources

try:
    flask_version = pkg_resources.get_distribution("flask").version
    pytube_version = pkg_resources.get_distribution("pytube").version
    print(f"flask version: {flask_version}")
    print(f"pytube version: {pytube_version}")
except pkg_resources.DistributionNotFound:
    print("pytube is not installed")



# def downloader():
#     link='https://youtu.be/wgBQkZjSbMQ'
#     yt = YouTube(link)
#     video = yt.streams.filter(only_audio=True).first()
#     out_file = video.download(output_path=".")
#     base, ext = os.path.splitext(out_file)
#     new_file = base + '.mp3'
#     os.rename(out_file, new_file)
