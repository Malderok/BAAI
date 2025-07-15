import os
from google import genai
from google.genai import types

def get_files_info(working_directory, directory=None):
    new_path = os.path.join(working_directory, directory)

    if not os.path.abspath(new_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(new_path):
        return f'Error: "{directory}" is not a directory'
    
    try:

        file_list = []

        for dir in os.listdir(new_path):
            dir_path = os.path.join(new_path, dir)
            dir_size = os.path.getsize(dir_path)
            is_dir = os.path.isdir(dir_path)  
            file_list.append(f"- {dir}: file_size={dir_size} bytes, is_dir={is_dir}")

        return "\n".join(file_list)
    
    except Exception as e:
        return f"Error listing files: {e}"
    
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)


    

    
    
    
