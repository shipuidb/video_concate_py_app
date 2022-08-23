import moviepy.editor
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, CompositeAudioClip

clip1 = VideoFileClip("one.mp4")
clip2 = VideoFileClip("two.mp4")
clip3 = VideoFileClip("three.mp4")

combined = concatenate_videoclips([clip1, clip2, clip3])
audio = AudioFileClip("intro.mp3")
combined.audio = CompositeAudioClip([audio])
combined.write_videofile("combined_01.mp4")
