import whisper
import math
from src.utils.secrets import Env

class Transcription(Env):
    def __init__(self) -> None:
        super().__init__()

    def format_time(seconds):
        hours = math.floor(seconds / 3600)
        seconds %= 3600
        minutes = math.floor(seconds / 60)
        seconds %= 60
        milliseconds = round((seconds - math.floor(seconds)) * 1000)
        seconds = math.floor(seconds)
        formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:01d},{milliseconds:03d}"
        return formatted_time

    def transcribe(self):
        model = whisper.load_model('base.en')
        result = model.transcribe(self.base_video)
        with open(self.srt_file, 'w+') as file1, open(self.timestamps_file, 'w+') as file2:
            for index, segment in enumerate(result['segments']):
                file1.write(str(index + 1) + '\n')
                file1.write(str(Transcription.format_time(segment['start'])) + ' --> ' + str(Transcription.format_time(segment['end'])) + '\n')
                file2.write(str(segment['start']) + '-' + str(segment['end']) + '\n')
                file1.write(segment['text'].strip()+ '\n')
                file1.write('\n')