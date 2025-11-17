import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.join(working_directory, file_path)
    absolute_directory = os.path.abspath(working_directory)
    absolute_path = os.path.abspath(full_path)
    if not absolute_path.startswith(absolute_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(absolute_path):
        return f'Error: File "{file_path}" not found.'
    if not absolute_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        combined_args = ["python", file_path] + list(args or [])
        execute = subprocess.run(
            combined_args,
            capture_output=True,
            timeout=30,
            cwd=absolute_directory,
            text=True,
        )

        out = execute.stdout or ""
        err = execute.stderr or ""

        if not out.strip() and not err.strip():
            return "No output produced."

        result = f"STDOUT: {out}\nSTDERR: {err}"
        if execute.returncode != 0:
            result += f"\nProcess exited with code {execute.returncode}"
        return result
    except Exception as e:
        return f'Error executing Python file: {e}'