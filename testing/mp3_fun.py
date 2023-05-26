import os

from pydub import AudioSegment

def convert_test():
    wav_audio = AudioSegment.from_file("H:\\m\\Sabaton\\fav\\Dreadnought.Flac", format="flac")
    wav_audio.export("H:\\m\\Sabaton\\flac_to_mp3\\Dreadnought.mp3", format="mp3")

def convert_folder():
    input_folder = "H:\\m\\Sabaton\\fav\\"
    output_folder = "H:\\m\\Sabaton\\flac_to_mp3"

    for root, dirs, files in os.walk(input_folder):
        for filename in files:
            if not filename.lower().endswith(".flac"):
                continue

            src_filepath = os.path.join(root, filename)
            wav_audio = AudioSegment.from_file(src_filepath, format="flac")

            mp3_filename = filename.replace('.flac', '.mp3')
            mp3_filename = mp3_filename.replace('.Flac', '.mp3')

            dst_filepath = os.path.join(output_folder, mp3_filename)

            wav_audio.export(dst_filepath, format="mp3")

convert_folder()



