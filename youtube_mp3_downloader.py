"""
pytube 를 이용하여, 유튜브 영상을 audio 형식의 mp4로 다운로드.
moviepy 를 이용하여, mp4를 mp3로 변환
"""

from pytube import Playlist, YouTube
from pytube.exceptions import VideoUnavailable
from moviepy.editor import *
import os
import sys
import string

output_path = "C:/Users/joong/Downloads/Marvel_Audio"

playlist_urls = [
    'https://www.youtube.com/playlist?list=PLWO-qREiYs0cGxkR4dqOl4btMpnXEbPo4',
    'https://www.youtube.com/playlist?list=PLiQQjRHXch0tpV3MUBNxwL_xiIjfgUM9V',
    'https://www.youtube.com/playlist?list=PLN4L7Z7A971jkhGwAHqFbP2U00AGkyKto',
    'https://www.youtube.com/playlist?list=PLsPGycGPtvl4Vyp54-ZwjyCKQdPofKJzl'
    ]

def youtube_audio_download_mp4(url, d_path):
    try:
        yt = YouTube(url)
    except VideoUnavailable:
        print(f'Video {url} is unavaialable, skipping.')
        return 1
    try:
        file_name = str(yt.title).replace(' ','_')
        for char in ['\\', '/', ':', '*', '?', '\"', '<', '>', '|']:
            file_name = file_name.replace(char, '')
        file_name = file_name + ".mp4"

        yt.streams.get_audio_only(subtype='mp4')
        print("\n***************************")
        print("Download starting...")
        print(f"URL : {url}")
        print(f"File Name : {file_name}")
        print(f"Download Path : {d_path}")
        print("***************************")
        yt.streams.first().download(
            output_path = d_path,
            filename = file_name
        )
        print("Download has done.")
        print("***************************\n")
        return 0
    except Exception as e:
        print(f"Erro : {e}")
        return 1

def MP4ToMP3(s_path, d_path, f_mp4):
    try:
        f_mp3 = f_mp4.split(".mp")[0] + ".mp3"
        FILETOCONVERT = AudioFileClip(os.path.join(s_path,f_mp4))
        FILETOCONVERT.write_audiofile(os.path.join(d_path,f_mp3))
        FILETOCONVERT.close()
        return "done"
    except Exception as e:
        return e

#####----- mp4 다운로드 -----#####
# playlist 다운로드
for i_folder, p_url in enumerate(playlist_urls):
    if i_folder==3:
        os.makedirs(output_path, eexist_ok=Tru)
        p_list = Playlist(p_url)
        print(f"Playlist URLs = {p_url}")
        for url in p_list.video_urls:
            print(f"URL = {url}")
            youtube_audio_download_mp4(url, output_path)
#개별 영상 다운로드
url = 'https://www.youtube.com/watch?v=LYM5KLeRoUA'
youtube_audio_download_mp4(url, output_path)
url = 'https://www.youtube.com/watch?v=oUGdSkdJrHw'
youtube_audio_download_mp4(url, output_path)
url = 'https://www.youtube.com/watch?v=LqAOpHJn5yg'
youtube_audio_download_mp4(url, output_path)

#####----- mp3로 변환 -----#####
mp4_path = output_path
mp3_path = os.path.join(mp4_path, "mp3")
os.makedirs(mp3_path, exist_ok=True)
for i, f_mp4 in enumerate(os.listdir(mp4_path)):
    print(i, f_mp4)
    ret = MP4ToMP3(mp4_path, mp3_path, f_mp4)
    print(ret)
