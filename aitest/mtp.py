# from pytube import YouTube

# # YouTube videonun URL'sini girin
# url = 'https://www.youtube.com/watch?v=HSNF8kiRe84'

# yt = YouTube(url)

# # Video dosyasını indirin
# video = yt.streams.first()
# video.download()

# print("Video indirme işlemi tamamlandı!")

# # ## Youtube video indirme kodu
# # pip install youtube-dl
# # youtube-dl https://www.youtube.com/watch?v=VIDEO_ID
import ffmpeg
input_file_name = 'washington.mp4'
(ffmpeg
 .input(input_file_name )
 .filter('fps', fps=1, round = 'up')
 .output("%s-%%04d.jpg"%(input_file_name[:-4]), **{'qscale:v': 3})
 .run())