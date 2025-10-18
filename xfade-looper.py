import soundfile as sf
import numpy as np

file = 'sweep_mono.wav'
fade_length_sec = 1.0

audio, fs = sf.read(file)

fade_length_samples = int(fs * fade_length_sec)

fade = np.linspace(0.0, 1.0, fade_length_samples)

fade_in = audio[:fade_length_samples] * fade
fade_out = audio[-fade_length_samples:] * np.flip(fade.copy())

xfade = fade_out + fade_in

out = audio[fade_length_samples:-fade_length_samples]
out = np.append(out, xfade)

sf.write('xfade.wav', out, fs)
