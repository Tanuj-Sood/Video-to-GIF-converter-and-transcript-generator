For both the methods python 3.x must be installed with the installation added to path (in environment variables).

METHOD 1-

Run "pip install -r requirements.txt" on command prompt to install all the necessary packages in your system

Run "pip install python-dotenv" on command prompt.

Run "choco install ffmpeg" on powershell (with administrator privileges) to install other dependencies.

Run the command "python main.py" on command prompt to run the code and when asked for the file name enter the file name (that must be present in the same folder as the main.py file.)
The output gifs get saved in the output folder.

METHOD 2-

Install anaconda navigator (download setup from website)

Under the environments panel click on import and locate the EXPORT.yaml file that is in the folder named "Export for Method 2"

After importing click on the run button beside te Videotogif environment and click on "open terminal"

Inside the terminal window write "cd {path to the folder where main.py is stored}" and press enter

Run "pip install python-dotenv" on command prompt (only the first time running the code not after that anymore).

After that follow from line 6 in the method 1
