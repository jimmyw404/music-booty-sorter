import re

class Cleaner:
    def __init__(self):
        print(f"Instantiated Cleaner")
        self.regexes = []

        # Remove "04-sabaton-" from "04-sabaton-the_unkillable_soldier.flac"
        self.regexes.append(r'^\d{2}-\w+-')

        # Remove  "01. " from "01. Introduction.mp3"
        self.regexes.append(r'^\d{2}\. ')

        # Remove "01-" from "01-Death Tone.mp3"
        self.regexes.append(r'^\d{2}\-')

        # Remove "01 - " from "01 - The Lord Of Steel.Mp3"
        self.regexes.append(r'^\d{2} - ')

        # Remove "03 – " from "03 – Never Forgotten Heroes.Mp3"
        self.regexes.append(r'^\d{2} – ')

        # Remove "02.- " from "02.- Emerald Sword.Mp3"
        self.regexes.append(r'^\d{2}\.-\s+')

        # Remove "03 " from "03 Queen Of The Dark Horizons.Mp3"
        self.regexes.append(r'^\d{2}\s')

    def is_song(self, filename):
        if filename.endswith(".mp3"):
            return True

        if filename.endswith(".flac"):
            return True

        return False

    def clean_filename(self, filename):
        cleaned = filename

        for regex in self.regexes:
            # Remove the matching pattern from the string
            cleaned = re.sub(regex, '', cleaned)

        # Capitalize
        cleaned = cleaned.title()

        # Print the updated string
        print(cleaned)
        return cleaned