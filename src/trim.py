import ffmpeg
import os
from src.utils.secrets import Env

class Trim(Env):
    def __init__(self) -> None:
        super().__init__()

    def trim(self):
        required_video_file = 'Subtitle_' + str(self.base_video)

        with open(self.timestamps_file) as f:
            times = f.readlines()

        times = [x.strip() for x in times] 

        dirname = 'output'
        if not os.path.isdir(dirname):
            os.mkdir(dirname)
        for time in times:
            output_path= str(dirname + '/' + str(times.index(time) + 1)) + ".gif"
            starttime = float(time.split("-")[0])
            endtime = float(time.split("-")[1])
            ffmpeg.input(required_video_file, ss=starttime, t=endtime-starttime).output(output_path).run()
  