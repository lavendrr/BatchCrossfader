import soundfile as sf
import numpy as np

file = 'sweep_mono.wav'
fade_length_sec = 1.0

audio, fs = sf.read(file)

fade_length_samples = int(fs * fade_length_sec)

valid_response = False
while valid_response == False:
    mode = input('Linear or equal power xfade? (enter L or EP): ')
    if mode == 'L':
        fade = np.linspace(0.0, 1.0, fade_length_samples)
        valid_response = True
    elif mode == 'EP':
        equal_power = lambda x: np.sqrt((1/2) * (1 + x))
        fade = np.apply_along_axis(equal_power, 0, np.linspace(-1.0, 1.0, fade_length_samples))
        valid_response = True
    else:
        print("Please enter L for linear or EP for equal power")

fade_in = audio[:fade_length_samples] * fade
fade_out = audio[-fade_length_samples:] * np.flip(fade)
xfade = fade_in + fade_out

out = audio[fade_length_samples:-fade_length_samples]
out = np.append(out, xfade)

sf.write('xfade.wav', out, fs)
