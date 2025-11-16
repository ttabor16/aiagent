import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    absolute_directory = os.path.abspath(working_directory)
    absolute_path = os.path.abspath(full_path)
    if not absolute_path.startswith(absolute_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    try:
        files = os.listdir(full_path)
        file_strings = []
        for file in files:
            file_path = os.path.join(full_path,file)
            file_string = f'- {file}: file_size: {os.path.getsize(file_path)}, is_dir={os.path.isdir(file_path)}'
            file_strings.append(file_string)
    
        return '\n'.join(file_strings)
    except Exception as e:
        return f"Error listing files: {e}"