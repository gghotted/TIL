from pytube import YouTube


url = 'https://www.youtube.com/watch?v=8Uv7hSif9SM'
yt = YouTube(url)

video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
print(video, '다운로드 시작')
video.download('')
print('다운로드 완료')

