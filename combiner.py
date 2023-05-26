import os
import shutil

from pydub import AudioSegment

import cleaner

class Combiner:
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir

        self.cleaner = cleaner.Cleaner()

        print(f"Combiner instantiated input_dir:[{self.input_dir}] output_dir:[{self.output_dir}]")

    def combine(self):
        print(f"Combining input:[{self.input_dir}] output:[{self.output_dir}]")

        # Recursively traverse the source directory
        for root, dirs, files in os.walk(self.input_dir):
            for filename in files:
                if not self.cleaner.is_song(filename):
                    continue

                # Construct the source and destination filepaths
                src_filepath = os.path.join(root, filename)

                cleaned_filename = self.cleaner.clean_filename(filename)

                dst_filepath = os.path.join(self.output_dir, cleaned_filename)

                # Handle name collisions by appending a number to the filename
                i = 1
                while os.path.exists(dst_filepath):
                    split = os.path.splitext(cleaned_filename)
                    dst_filepath = os.path.join(self.output_dir, split[0] + "_" + str(i) + split[1])
                    i += 1

                if filename.lower().endswith(".flac"):
                    input_audio = AudioSegment.from_file(src_filepath, format="flac")
                    input_audio.export(dst_filepath, format="mp3")
                else:
                    # Copy the file to the destination directory
                    shutil.copy2(src_filepath, dst_filepath)
