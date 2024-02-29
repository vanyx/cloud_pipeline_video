from moviepy.editor import VideoFileClip

import datetime
import speech_recognition as sr
import os
import time


class SubtitlePod:
    def __init__(self, video_path: str, audio_path: str) -> None:
        self.video_path = video_path
        self.video = VideoFileClip(video_path)
        self.audio_path = audio_path
        self.srt_path = None
        self.srt_block_num = 1

    def set_srt_path(self, filename: str) -> None:
        self.srt_path = filename

    def speech_to_srt(self, current_time: datetime.datetime, block_num: int):
        r = sr.Recognizer()
        with sr.AudioFile(self.audio_path) as source:
            if (
                (current_time.hour*3600 + current_time.minute*60 + current_time.second + 4)
                < 
                self.video.duration
            ):
                r.adjust_for_ambient_noise(source)
                offset = current_time.minute*60 + current_time.second + current_time.microsecond/1000000
                print(str(current_time + datetime.timedelta(seconds=4)) + " -- " + str(datetime.datetime.fromtimestamp(self.video.duration)))
                data = r.record(source, duration=4, offset=offset)
                try:
                    text = r.recognize_whisper(data)
                except sr.UnknownValueError:
                    print("Audio error")
                except sr.RequestError:
                    print("Request error")
            elif (
                (current_time.hour*3600 + current_time.minute*60 + current_time.second)
                < 
                self.video.duration
            ):
                r.adjust_for_ambient_noise(source)
                offset = current_time.minute*60 + current_time.second + current_time.microsecond/1000000
                print(str(current_time) + " --- " + str(datetime.datetime.fromtimestamp(self.video.duration)))
                data = r.record(source, offset=offset)
                try:
                    text = r.recognize_whisper(data)
                except sr.UnknownValueError:
                    print("Audio error")
                except sr.RequestError:
                    print("Request error")
            else:
                return None

        end_time = current_time + datetime.timedelta(seconds=4)

        str_current_time = str(current_time.time())
        str_end_time = str(end_time.time())

        with open(self.srt_path, 'a', encoding='utf-8') as f:
            f.write(f"{str(block_num)}")
            f.write(f"\n")
            f.write(f"{str_current_time},000")
            f.write(f" --> ")
            f.write(f"{str_end_time},000")
            f.write(f"\n")
            f.write(f"{text}")
            f.write(f"\n")
            f.write(f"\n")

        return self.speech_to_srt(end_time, block_num + 1)
    
    def create_subtitles(self, srt_filename: str) -> None:
        self.set_srt_path(srt_filename)
        self.speech_to_srt(datetime.datetime(1970, 1, 1, 0, 0, 0), self.srt_block_num)


video_path = "/app/results/capybara_resized.mp4"
audio_path = "/app/results/capybara_audio.wav"
subtitle_path = "/app/results/capybara_subtitles.srt"
video_subtitled_path = "/app/results/capybara_subtitled.mp4"

#wait for the video to be released
while not os.path.exists("/app/tmp/langident_finish.txt"):
    time.sleep(1)

#delete the file if it exists
os.remove("/app/tmp/langident_finish.txt")

subtitle_pod1 = SubtitlePod(video_path, audio_path)
subtitle_pod1.create_subtitles(subtitle_path)
os.system(f"ffmpeg -i {video_path} -vf subtitles={subtitle_path} {video_subtitled_path}")
with open("/app/tmp/subtitle_finish.txt", "w") as indicator_file:
    indicator_file.write("Subtitle finished.")