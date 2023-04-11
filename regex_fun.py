import re
import os
import shutil

def unkillable_soldier_test():
    # Define the string
    string = "04-sabaton-the_unkillable_soldier.flac"

    # Define the regular expression pattern
    pattern = r'^\d{2}-\w+-'

    # Remove the matching pattern from the string
    new_string = re.sub(pattern, '', string)

    # Replace the '_' with spaces
    new_string = new_string.replace('_', ' ')

    new_string = new_string.title()

    # Print the updated string
    print(new_string)

def combine_test():
    # Specify the source and destination directories
    src_directory = "H:/m/Sabaton/saba_disco_test_input"
    dst_directory = "H:/m/Sabaton/saba_disco_test_output"

    # Recursively traverse the source directory
    for root, dirs, files in os.walk(src_directory):
        for file in files:
            # Construct the source and destination filepaths
            src_filepath = os.path.join(root, file)
            dst_filepath = os.path.join(dst_directory, file)

            # Handle name collisions by appending a number to the filename
            i = 1
            while os.path.exists(dst_filepath):
                split = os.path.splitext(file)
                dst_filepath = os.path.join(dst_directory, split[0] + "_" + str(i) + split[1])
                i += 1

            # Copy the file to the destination directory
            shutil.copy2(src_filepath, dst_filepath)



# unkillable_soldier_test()
combine_test()