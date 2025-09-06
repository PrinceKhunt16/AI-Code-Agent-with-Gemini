import os 
from functions.get_files_info import get_files_info, schema_get_files_info
from functions.get_file_content import get_file_content, schema_get_file_content
from functions.write_file import write_file, schema_write_file
from functions.run_python_files import run_python_file, schema_run_python_file
from functions.delete_file import delete_file, schema_delete_file
from functions.create_folder import create_folder, schema_create_folder
from functions.delete_folder import delete_folder, schema_delete_folder
from google.genai import types
 
# working_directory = "calculator"

working_directory = os.path.dirname(os.path.abspath(__file__))

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    
    result = ""

    if function_call_part.name == "get_files_info":
        result = get_files_info(working_directory, **function_call_part.args)
       
    if function_call_part.name == "get_file_content":
        result = get_file_content(working_directory, **function_call_part.args)
        
    if function_call_part.name == "write_file":
        result = write_file(working_directory, **function_call_part.args)
        
    if function_call_part.name == "run_python_file":
        result = run_python_file(working_directory, **function_call_part.args)

    if function_call_part.name == "delete_file":
        result = delete_file(working_directory, **function_call_part.args)

    if function_call_part.name == "create_folder":
        result = create_folder(working_directory, **function_call_part.args)
    
    if function_call_part.name == "delete_folder":
        result = delete_folder(working_directory, **function_call_part.args)
        
    if result == "":
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )
    
    return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"result": result},
                )
            ],
        )