from pytube import request
from pytube import YouTube
import tempfile
import shutil


url = 'https://www.youtube.com/watch?v=8Uv7hSif9SM'
yt = YouTube(url)
video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
with tempfile.NamedTemporaryFile(delete=False) as f:
    for chunk in request.stream(video.url):
        f.write(chunk)
filename = f.name

shutil.copyfile(filename, 'test.mp4')

