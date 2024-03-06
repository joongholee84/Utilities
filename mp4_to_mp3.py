from moviepy.editor import *
import os
import sys
import shutil

def MP4ToMP3(s_path, d_path, f_mp4):
    try:
        f_mp3 = f_mp4.split(".mp")[0] + ".mp3"
        FILETOCONVERT = AudioFileClip(os.path.join(s_path,f_mp4))
        FILETOCONVERT.write_audiofile(os.path.join(d_path,f_mp3))
        FILETOCONVERT.close()
        return "done"
    except Exception as e:
        return e

s_path = r"C:\Users\joong\Downloads\disney"
d_path = r"C:\Users\joong\Downloads\disney\result"
os.makedirs(d_path, exist_ok=True)
input("press any key")

for i, f_mp4 in enumerate(os.listdir(s_path)):
    print(i, f_mp4)
    ret = MP4ToMP3(s_path, d_path, f_mp4)
    print(ret)
