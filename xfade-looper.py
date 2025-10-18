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

sf.write('xfade-linear.wav', out, fs)

# Equal Power

fade = np.linspace(-1.0, 1.0, fade_length_samples)

equal_power_fade_in = lambda x: np.sqrt((1/2) * (1 + x))

fade_in = audio[:fade_length_samples] * np.apply_along_axis(equal_power_fade_in, 0, fade)
fade_out = audio[-fade_length_samples:] * np.apply_along_axis(equal_power_fade_in, 0, np.flip(fade))

xfade = fade_in + fade_out

out = audio[fade_length_samples:-fade_length_samples]
out = np.append(out, xfade)

sf.write('xfade-equalpower.wav', out, fs)

