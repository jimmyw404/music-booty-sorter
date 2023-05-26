import re

class Cleaner:
    def __init__(self):
        print(f"Instantiated Cleaner")
        # https://i.redd.it/gu4n3392l4w61.png
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

        # Remove "101-" from "101-Powerwolf-Faster_Than_The_Flame.Flac"
        self.regexes.append(r'^\d+-')

        # Remove "Powerwolf-" from "101-Powerwolf-Faster_Than_The_Flame.Flac"
        self.regexes.append(r"^Powerwolf-")

    def is_song(self, filename):
        if filename.lower().endswith(".mp3"):
            return True

        if filename.lower().endswith(".flac"):
            return True

        return False

    def clean_filename(self, filename):
        cleaned = filename

        for regex in self.regexes:
            # Remove the matching pattern from the string
            cleaned = re.sub(regex, '', cleaned)

        # Faster Than The Flame.Flac -> Faster Than The Flame.Flac
        cleaned = cleaned.replace('_', ' ')

        # Faster Than The Flame.Flac -> Faster Than The Flame.mp3
        if cleaned.lower().endswith(".flac"):
            cleaned = cleaned.replace('.flac', '.mp3')
            cleaned = cleaned.replace('.Flac', '.mp3')

        # Capitalize
        cleaned = cleaned.title()

        # Print the updated string
        print(cleaned)
        return cleaned
