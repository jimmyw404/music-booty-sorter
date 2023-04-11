import re

class Cleaner:
    def __init__(self):
        print(f"Instantiated Cleaner")
        self.regexes = []

        # Remove "04-sabaton-" from "04-sabaton-the_unkillable_soldier.flac"
        self.regexes.append(r'^\d{2}-\w+-')

        # Remove  "01. " from "01. Introduction.mp3"
        self.regexes.append(r'^\d{2}\. ')

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