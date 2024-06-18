import os
from src.utils.secrets import Env
import ffmpeg

class Subtitle(Env):
    def __init__(self) -> None:
        super().__init__()

    def subtitle(self):
        output_video_name = 'Subtitle_' + str(self.base_video)
        #os.popen(f"ffmpeg -i {self.base_video} -vf subtitles={self.srt_file} {output_video_name}")
        ffmpeg.input(self.base_video).output(output_video_name, vf=f'subtitles={self.srt_file}').run(overwrite_output=True)