import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f"Error: {file_path} is not in the directory."
    
    if not os.path.isfile(abs_file_path):
        return f"Error: {file_path} is not a file."

    try:
        with open(abs_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

            if len(file_content_string) >= MAX_CHARS:
                file_content_string += (
                    f'...File {file_path} is trancated at 10000 character.'
                )
    except Exception as e:
        print("Error: This error from get_file_content function.")
        return f"Exception reading file: {e}"

    return file_content_string

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Get the content of the given file as a string, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read, relative to the working directory.",
            ),
        },   
        required=["file_path"],
    ),
)