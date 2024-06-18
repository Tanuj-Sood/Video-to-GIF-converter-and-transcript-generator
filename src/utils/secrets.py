import os
from dotenv import load_dotenv

class Env():
    def __init__(self) -> None:
        load_dotenv()
        self._base_video = os.environ.get("BASE_VIDEO")
        self._transcription_file = os.environ.get("TRANSCRIPTION_FILE")
        self._timestamps_file = os.environ.get("TIMESTAMP_FILE")
        self._srt_file = os.environ.get("SRT_FILE")

    @property
    def base_video(self):
        return self._base_video

    @property
    def transcription_file(self):
        return self._transcription_file

    @property
    def timestamps_file(self):
        return self._timestamps_file
    
    @property
    def srt_file(self):
        return self._srt_file