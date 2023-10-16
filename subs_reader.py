# %%
import os
from openpyxl import Workbook
import validators
from formatting import format_header


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

# %%


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

# %%


def read_files(file_dir):
    """Read file content and prepare for saving to Excel"""
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            # Check if file is a subtitle file
            if file.split(".")[-1] in ["vtt", "srt"]:
                file_path = os.path.join(root, file)

                with open(file_path, 'r', encoding='utf-8') as file:
                    file_content = [line for line in file]

                    with_counts = [[
                        text, '',
                        f'=LEN(A{i+1})',
                        f'=LEN(B{i+1})',
                        f'=IF(LEN(B{i+1})>LEN(A{i+1}),"Too long", "Ok")'] for i, text in enumerate(file_content, 1)]

                    save_file_list_to_excel(with_counts, file)



def save_file_list_to_excel(content, file):
    """Save filenames to Excel file"""
    wb = Workbook()
    ws = wb.active
    wb.create_sheet()
    
    ws.append(["Source", "Translation", "Source count", "Target count"])
    format_header(ws)
    
    for row in content:
        ws.append(row)

    wb.save(filename=f"{file.name}.xlsx")


file_dir = get_path_to_folder()
read_files(file_dir)

# %%
