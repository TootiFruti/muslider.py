#!/usr/bin/python3

import subprocess
import os
from sys import argv

audio_extensions = (".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a")
video_extensions = (
    ".mp4", ".mkv", ".mov", ".avi", ".flv", ".wmv",
    ".webm", ".mpeg", ".mpg", ".3gp", ".m4v"
)

def get_all_paths(root_dir):
    paths = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for name in dirnames + filenames:
            paths.append(os.path.join(dirpath, name))
    return paths

root_directory =
all_paths = get_all_paths(root_directory)

dest = argv[2]

vids = []
audios = []

for i in all_paths:
    if i.endswith(audio_extensions):
        audios.append(i)

    if i.endswith(video_extensions):
        vids.append(i)

for i in audios:
    subprocess.run(["cp", "-v", i, dest])

for i in vids:
    dest_path = f"{dest}{os.path.splitext(os.path.basename(i))[0]}.mp3"

    subprocess.run(["ffmpeg", "-i", i, dest_path])




