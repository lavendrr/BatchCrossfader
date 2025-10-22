# BatchCrossfader v1.1
# Ricardo Moctezuma 2025

import soundfile as sf
import numpy as np
import os
from glob import iglob

version = 1.1

equal_power = lambda x: np.sqrt((1/2) * (1 + x))

def xfade_process(channel, fade, fade_length_samples):
    fade_in = channel[:fade_length_samples] * fade
    fade_out = channel[-fade_length_samples:] * np.flip(fade)
    xfade = fade_in + fade_out

    prefade = channel[fade_length_samples:-fade_length_samples]
    return np.append(prefade, xfade)

print(f'--- Welcome to BatchCrossfader v{version}! --- \nPlace files you\'d like to process in the File Input folder. See ReadMe.txt for usage instructions & general info.')

valid_response = False
while valid_response == False:
    fade_length_sec = float(input("\nPlease enter the desired crossfade length in seconds as a positive integer or decimal number: "))
    if not ((isinstance(fade_length_sec, int) or isinstance(fade_length_sec, float)) and fade_length_sec > 0):
        print('\n> Please make sure to enter a positive integer or decimal number')
    else:
        valid_response = True

valid_response = False
while valid_response == False:
    mode = input('\nLinear or equal power crossfade? (enter L or EP): ').upper()
    if mode not in ['L', 'EP']:
        print('\n> Please make sure to enter L for linear or EP for equal power')
    else:
        valid_response = True
    
valid_response = False
while valid_response == False:
    in_format = input('\nPlease enter the input file format (e.g. .wav, .mp3, .flac, etc.): ')
    if in_format.strip('.').upper() not in sf.available_formats().keys():
        print('\n> Please make sure to enter a supported file format - see python-soundfile docs for supported formats (https://python-soundfile.readthedocs.io/en/0.13.1/_modules/soundfile.html#available_formats)')
    else:
        valid_response = True

if not os.path.exists('Crossfade Output'):
    os.makedirs('Crossfade Output')

exec = False
print('\nBeginning crossfade processing...\n')

for file in iglob(f'File Input/**/*{in_format.lower()}', recursive = True):
    if not exec:
        exec = True

    file = file.replace('\\', '/')
    file_directory, *_, file_name = file.rpartition('/')
    file_directory = file_directory.strip('File Input/').strip('/..')
    if file_directory != '':
        file_directory += '/'
        if not os.path.exists(f'Crossfade Output/{file_directory}'):
            os.makedirs(f'Crossfade Output/{file_directory}')

    audio, fs = sf.read(file)
    fade_length_samples = int(fs * fade_length_sec)

    if mode == 'L':
        fade = np.linspace(0.0, 1.0, fade_length_samples)
    elif mode == 'EP':
        fade = np.apply_along_axis(equal_power, 0, np.linspace(-1.0, 1.0, fade_length_samples))
    try:
        output = np.apply_along_axis(xfade_process, 0, audio, fade = fade, fade_length_samples = fade_length_samples)
        sf.write(f'Crossfade Output/{file_directory}xfade-{file_name}', output, fs)
        print(f'Saved xfade-{file_name} to Crossfade Output/{file_directory}')
    except ValueError:
        print(f'Unable to execute for {file_name} due to fade length being too long - ensure that files are at least twice as long as the fade length')

if not exec:
    print('\nNo matching files found! \nPlease ensure that all files are located in a folder called \'File Input\' and that you have entered the matching file format')
else:
    print('\nAll done! Output files can be found in the Crossfade Output folder')
