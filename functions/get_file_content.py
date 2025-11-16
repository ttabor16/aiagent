import os
from functions.config import MAX_CHARS

def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    absolute_directory = os.path.abspath(working_directory)
    absolute_path = os.path.abspath(full_path)
    if not absolute_path.startswith(absolute_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(absolute_path,"r") as f:
            file_content_string = f.read(MAX_CHARS)
        return file_content_string
    except Exception as e:
        return f"Error reading file: {e}"

