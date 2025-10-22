BatchCrossfader v1.0
Ricardo Moctezuma 2025

### Overview ###

BatchCrossfader is a script that crossfades a sound file's end with its beginning, allowing for seamless looping of the asset for sound design or similar applications. To achieve this, the program removes a certain length from the beginning of the file and pastes it over the same length at the end of the file with a crossfade applied, so that, when looped, the end and beginning will seamlessly transition into each other.

### Install ###
- Download the correct version for your platform from the Releases page and extract it
- Mac: Open Terminal, navigate to the extracted folder using the `cd` command, and run the install.sh script via the command `./install.sh` (without the `)
- Windows: Open Command Prompt, navigate to the extracted folder using the `cd` command, and run the install.bat script via the command `call install.bat` (without the `)
- Once this has finished, you can safely delete the install script and the .tar file if desired
- To run the script, just call run.sh or run.bat via the command line in the same way you ran the install script

### Usage ###

- Place the files you wish to use in the `File Input` folder. You can use sub-folders within `File Input` if you want to keep your sounds categorized - the hierarchy will be recreated in the output folder.
- Run the run.sh or run.bat file via the command line
- Enter the desired options when prompted
- Files will be output in the `Crossfade Output` folder following the same folder hierarchy and name (prefixed with 'xfade-') used in the `File Input` folder

### Options ###

- Fade Length: The length of the crossfade, expressed in seconds as a positive integer or decimal number. All input files must be at least twice as long as the fade length, since the program will be cutting this length off of the beginning and crossfading it with this length at the end.
- Mode: The type of crossfade applied - `L` for linear, `EP` for equal power. 
	- Linear, or equal gain, crossfades use a directly inverse relationship between the two signals and maintain a uniform gain on the volume meter. This will, however, result in a perceptual dip in volume in the middle of the crossfade, where each signal is at 0.5 gain, and may be more noticeable.
	- Equal power crossfades scale off of the square root of 1/2 and meet in the middle with each signal being roughly 0.707 gain. This will result in a higher gain in the middle and could possibly result in clipping, but maintains a uniform perceptual volume.
- File Extension: The type of file you want to process, expressed as a string input such as `.wav`, 'WAV', `.mp3`, 'MP3', etc. All files with this file extension in the `File Input` folder will be processed. Files will be output in the same format they were input. For a list of available formats, check the py-soundfile documentation at https://python-soundfile.readthedocs.io/en/0.13.1/_modules/soundfile.html#available_formats

### Contact/End Note ###

If you experience any issues or have any feedback, please contact me at rmoctezumaf@gmail.com! Feel free to view my other programming and sound work on my website, ricardomoctezuma.com. Thank you for using BatchCrossfader! :)
