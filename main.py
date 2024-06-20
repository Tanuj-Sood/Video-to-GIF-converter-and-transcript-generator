from src.subtitle import Subtitle
from src.transcription import Transcription
from src.trim import Trim
import dotenv
import os


subtitle = Subtitle()
transcription = Transcription()
trim = Trim()

def run():
    #code for getting user inputted filename
    #filename= str(input("Enter File name:-"))
    #dotenv_file = dotenv.find_dotenv()
    #dotenv.load_dotenv(dotenv_file)

    #os.environ["BASE_VIDEO"] = filename
    # Write changes to .env file.
    #dotenv.set_key(dotenv_file, "BASE_VIDEO", os.environ["BASE_VIDEO"])

    #calling of the functions
    transcription.transcribe()
    subtitle.subtitle()
    trim.trim()

if __name__ == "__main__":
    run()
