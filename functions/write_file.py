import os
from google import genai
from google.genai import types


def write_file(working_directory, file_path, content):
    new_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not new_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(new_path):
        try:
            os.makedirs(os.path.dirname(new_path), exist_ok=True)
        except Exception as e:
            return f"Error: creating directory: {e}"    
    
        
    if os.path.exists(new_path) and os.path.isdir(new_path):
        return f'Error: "{file_path}" is a directory, not a file'
    



        
    try:

        with open(new_path, "w") as file:
            file.write(content)

    except Exception as e:
        return f"Error: {e}"
    
    # try:

    #     with open(new_path, "w") as file:
    #         file.write(content)
    
    # except Exception as e:
    #     return f"Error: {e}"
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'



schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Lists content in files.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Write to the file, relative to the working directory. If not provided, write a new file in the working directory itself.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that will be writen",
            ),
        },
    ),
)

