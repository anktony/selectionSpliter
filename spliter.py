from pydub import AudioSegment
import subprocess
import os

def convert_to_mp3(input_file, output_file):
    subprocess.run(['ffmpeg', '-i', input_file, output_file])

def split_and_convert(input_file, split_points):
    audio = AudioSegment.from_file(input_file, format="aac")

    for start_time, end_time, output_name in split_points:
        start_ms = sum(x * int(t) for x, t in zip([3600, 60, 1], start_time.split(":"))) * 1000
        end_ms = sum(x * int(t) for x, t in zip([3600, 60, 1], end_time.split(":"))) * 1000

        segment = audio[start_ms:end_ms]
        output_name_mp3 = os.path.splitext(output_name)[0] + ".mp3"
        segment.export(output_name_mp3, format="mp3")
        print(f"Converted {output_name} to {output_name_mp3}")

if __name__ == "__main__":
    input_file = "selecao camaradas.aac"

    split_points = [
        ("00:40:33", "00:44:21", "Ogum em seu cavalo.aac")
    ]

    split_and_convert(input_file, split_points)
