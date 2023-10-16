#%%
import os
import validators

"""
1. Get a path to the folder - validate if valid path (separate function / module)
2. Select path for the target file
3. Interate over all files in a folder that are subtitles:
- check if file  (vtt or srt):
    - for each file that is, read line by line and write to Excel
    - A = Source
    - B = Target
    - C = Source Length (`=LEN(A{i+1})`)
    - D = Target Length (`=LEN(B{i+1})`)
    - E = count ('=IF(LEN(B{i+1})>LEN(A{i+1}),"Too long", "Ok")')
- if no files, go back to getting path
"""

#%%
def get_path_to_folder():
    """Ask user to provide path"""
    while True:
        path_input = input(
            "Path to the folder with subtitles: ")
        try:
            folder_path = validators.validate_file_path(path_input)
        except ValueError as error:
            print(f"{error} Try again.\n")
            continue
        print("this is the path you provided")
        return folder_path

get_path_to_folder()
# %%

