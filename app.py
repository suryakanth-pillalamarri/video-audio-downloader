from flask import Flask, request, send_file
import os
from pytube import YouTube

app = Flask(__name__)

class Youtube:
    def video_downloader(self, link, path):
        yt = YouTube(link)
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path=path)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        return new_file

y = Youtube()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        link = request.form['link']
        path = request.form['path']
        file_path = y.video_downloader(link, path)
        return send_file(file_path, as_attachment=True)
    return '''
        <form method="post">
            Enter youtube video link: <input type="text" name="link">
            <input type="submit" value="Download">
            Enter the path to download the file: <input type="text" name="path">
        </form>
    '''

if __name__ == '__main__':
    app.run()
