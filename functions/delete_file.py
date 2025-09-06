import os
from google.genai import types

def delete_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f"Error: {file_path} is not in the directory."
    
    if not os.path.isfile(abs_file_path):
        return f"Error: {file_path} is not a file."

    try:
        os.remove(abs_file_path)
        return f"Successfully deleted {file_path}"
    except Exception as e:
        print("Error: This error from delete_file function.")
        return f"Error: failed to delete file {e}"
    
schema_delete_file = types.FunctionDeclaration(
    name="delete_file",
    description="Deletes a specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to delete."
            )
        },   
        required=["file_path"],
    ),
)