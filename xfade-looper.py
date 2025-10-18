import soundfile as sf
import numpy as np
import os
from glob import glob

equal_power = lambda x: np.sqrt((1/2) * (1 + x))

fade_length_sec = float(input('Please enter the desired crossfade length in seconds as a decimal number or integer: '))

valid_response = False
while valid_response == False:
    mode = input('Linear or equal power xfade? (enter L or EP): ')
    if mode not in ['L', 'EP']:
        print("Please enter L for linear or EP for equal power")
    else:
        valid_response = True

if not os.path.exists('Crossfade Output'):
    os.makedirs('Crossfade Output')

for file in glob('*.wav'):
    audio, fs = sf.read(file)

    fade_length_samples = int(fs * fade_length_sec)

    if mode == 'L':
        fade = np.linspace(0.0, 1.0, fade_length_samples)
    elif mode == 'EP':
        fade = np.apply_along_axis(equal_power, 0, np.linspace(-1.0, 1.0, fade_length_samples))

    fade_in = audio[:fade_length_samples] * fade
    fade_out = audio[-fade_length_samples:] * np.flip(fade)
    xfade = fade_in + fade_out

    out = audio[fade_length_samples:-fade_length_samples]
    out = np.append(out, xfade)

    sf.write(f'Crossfade Output/xfade-{file}', out, fs)

print('Saved files to /Crossfade Output')
