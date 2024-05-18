# OLLM
OLLM is a tool for detecting functional bugs in Android apps.
source code for OLLM


##How to set up OLLM on a new PC:

Create Android Emulator Pixel 2, API 28， Android 9.0 ('Pie') x86 on Android Studio

Download and Install Visual Studio code, following: https://code.visualstudio.com/docs/python/python-tutorial complete the section 'create a virtual environment' use venv as virtual enviroment

In vs code, search extension, Install Jupyter extension in vs code

In vs code command line: pip install uiautomator pip install uiautomator2 pip install -U weditor

ps. In the above steps some dialog will show up, here is how you should select: Kerne dialog: Choose Python environments .venv Dailog: install ipykernal package? yes

Get the emulator device number, in linux cmd run ’adb devices’, replace the number in d = Device("emulator-5554") in the 2nd code block with the device number of your own

Install apk and drag apk into the emulator. Open the app in your emulator

Go back to vscode, open the terminal, run code: sudo apt-get install --reinstall python-pkg-resources, pip install setuptools, python3 -m editor

In the same category with the ipynb file, create a txt file named action.txt, and store the action text in it.

Change folder name in script, the varable folder_name = 'XXX', XXX is the id of the bug

Run script code blocks
