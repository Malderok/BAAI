import os
from google import genai
from google.genai import types

from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file

from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file


available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
        
    ]
)

def call_function(function_call_part, verbose=False):

    funcs = {
        "get_file_content": get_file_content,
        "get_files_info": get_files_info,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }

    function_call_part.args["working_directory"] = "./calculator"

    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})\n")
    else:
        print(f" - Calling function: {function_call_part.name}\n") 


    if funcs[function_call_part.name]:

        function_result = funcs[function_call_part.name](**function_call_part.args)

        return types.Content(
        role="tool",
        parts=[
        types.Part.from_function_response(
            name=function_call_part.name,
            response={"result": function_result},
        )
    ],
)
    
    else:

        return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"error": f"Unknown function: {function_name}"},
            )
        ],
    )





# def really_call_function(name):

#     case