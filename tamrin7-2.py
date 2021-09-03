 from moviepy import editor
video = editor.VideoFileClip("C:\Users\Me\sesoin1\estor\hoomayun.mp4.mkv")
video.audio.write_audiofile("C:\Users\Me\sesoin1\estor\hoomayun.mp3")