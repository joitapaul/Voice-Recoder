import sounddevice
from scipy.io.wavfile import 


fps =44100
duration = 10
print("RECORDING...")
recording = sounddevice.rec(int(duration*fps), samplerate=fps, channels=2)
sounddevice.wait()
print("Done!")

write("Output.wav",fps, recording)
