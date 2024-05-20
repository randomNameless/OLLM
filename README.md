# OLLM
OLLM is a tool for detecting functional bugs.
source code for OLLM

## Artifact Description
This is the artifact for the paper: Detecting Non-Crash Functional Bugs in Android Apps Using Multimodal Large Language Models

The artifact shows:

1) Source code for OLLM (./code/)
2) Experiment results generated by OLLM presented in the paper(./Experiments/Prompt Feedback/).
3) Programs (i.e., APKs), bug reports and prompts generated in the paper (./Experiments/Bug Reproduction and Prompt Genaration/).
4) Documentation showing how OLLM can be used.

## Run OLLM
1) Create Android Emulator Pixel 2, API 28， Android 9.0 ('Pie') x86 in Android Studio, and open the emulator.

2) Get the emulator device number, in linux cmd run ’adb devices’, replace the number in d = Device("emulator-5554") in the source code with the device number of your own.

3) Install apk and drag apk into the emulator. Open the app in your emulator.

4) In the same category with the source code file, create a txt file named action.txt, and store the action text in it. the format of the action text should be 'Action NameOfUIElement'
   For Example:
```sh
click Allow
click Allow
click com.ichi2.anki:id/action_sync
click LOG IN
click Email address
```
6) Change the folder name in the script for each bug, the variable folder_name = 'XXX', XXX is the id of the bug.

## Description of Result Files Generated By OLLM:
We took the bug
