import os
import string
import subprocess
from google import genai
from google.genai import types

from functions.write_file import write_file
from config import MAX_CHARS

def run_python_file(working_directory, file_path):
    new_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not new_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if os.path.isfile(new_path):
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'      
        try:
            output = []
            result = subprocess.run(["python", file_path], capture_output=True ,cwd=working_directory ,timeout=30, text=True)



            if len(result.stdout) == 0 and len(result.stderr) == 0 :
                return "No output produced."
            
            stdout_out = "STDOUT:" + result.stdout
            stderr_out = "STDERR:" + result.stderr

            output.append(stdout_out)
            output.append(stderr_out)
            if result.returncode != 0:

                output.append(f"Process exited with code {result.returncode}")

            return "\n".join(output)
        except Exception as e:
            return f"Error: executing Python file: {e}"
        
    else:

        return f'Error: File "{file_path}" not found.'
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run code in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Run code inside the working directory.",
            ),
        },
    ),
)