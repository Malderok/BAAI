import os
from config import MAX_CHARS
from google import genai
from google.genai import types

def get_file_content(working_directory, file_path):
    new_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not new_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(new_path):
        
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:

        dir_size = os.path.getsize(new_path)

        with open(new_path, "r") as f:
            if dir_size > MAX_CHARS:

                result = f.read(MAX_CHARS) + f"...File {file_path} truncated at 10000 characters"


                return result

            return f.read()


    
    except Exception as e:
        return f"Error: {e}"
    


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Lists file content.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file relative to the working directory.",
            ),
        },
    ),
)