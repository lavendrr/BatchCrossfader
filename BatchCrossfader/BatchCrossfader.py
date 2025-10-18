import soundfile as sf
import numpy as np
import os
from glob import iglob

equal_power = lambda x: np.sqrt((1/2) * (1 + x))

def xfade_process(channel, fade, fade_length_samples):
    fade_in = channel[:fade_length_samples] * fade
    fade_out = channel[-fade_length_samples:] * np.flip(fade)
    xfade = fade_in + fade_out

    prefade = channel[fade_length_samples:-fade_length_samples]
    return np.append(prefade, xfade)

fade_length_sec = float(input('Please enter the desired crossfade length in seconds as a decimal number or integer: '))

valid_response = False
while valid_response == False:
    mode = input('Linear or equal power xfade? (enter L or EP): ')
    if mode not in ['L', 'EP']:
        print("Please enter L for linear or EP for equal power")
    else:
        valid_response = True
    
valid_response = False
while valid_response == False:
    in_format = input('Please enter the input file format (e.g. .wav, .mp3, .flac, etc.): ')
    if in_format.strip('.').upper() not in sf.available_formats().keys():
        print("Please enter a supported file format - see python-soundfile docs for supported formats (https://python-soundfile.readthedocs.io/en/0.13.1/_modules/soundfile.html#available_formats)")
    else:
        valid_response = True

if not os.path.exists('Crossfade Output'):
    os.makedirs('Crossfade Output')

for file in iglob(f'../**/*{in_format}', recursive = True):
    if not file.startswith('../BatchCrossfader/Crossfade Output/'):
        file_directory, file_name = '', file
        if '/' in file:
            file_directory, *_, file_name = file.rpartition('/')
            file_directory = file_directory.strip('/..') + '/'
            if not os.path.exists(f'Crossfade Output/{file_directory}'):
                os.makedirs(f'Crossfade Output/{file_directory}')

        audio, fs = sf.read(file)

        fade_length_samples = int(fs * fade_length_sec)

        if mode == 'L':
            fade = np.linspace(0.0, 1.0, fade_length_samples)
        elif mode == 'EP':
            fade = np.apply_along_axis(equal_power, 0, np.linspace(-1.0, 1.0, fade_length_samples))

        output = np.apply_along_axis(xfade_process, 0, audio, fade = fade, fade_length_samples = fade_length_samples)

        sf.write(f'Crossfade Output/{file_directory}{file_name}', output, fs)

print('Saved files to /Crossfade Output')
