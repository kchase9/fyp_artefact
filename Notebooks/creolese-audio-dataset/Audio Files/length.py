import os
import wave

folder_path = "."  # Replace this with your actual path
audio_files = [f for f in os.listdir(folder_path) if f.endswith(".wav")]

# Sort by the numeric part of the filename
audio_files.sort(key=lambda x: int(os.path.splitext(x)[0]))

total_duration = 0.0

for f in audio_files[:36]:
    with wave.open(os.path.join(folder_path, f), 'r') as wf:
        frames = wf.getnframes()
        rate = wf.getframerate()
        duration = frames / float(rate)
        print(f"{f}: {duration:.2f} seconds")
        total_duration += duration

print(f"\nTotal duration: {total_duration:.2f} seconds ({total_duration / 60:.2f} minutes)")
