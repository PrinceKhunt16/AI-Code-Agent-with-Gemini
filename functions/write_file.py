import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f"Error: {file_path} is not in the directory."

    parent_dir = os.path.dirname(abs_file_path)

    if not os.path.exists(parent_dir):
        try:
            os.makedirs(parent_dir, exist_ok=True)
        except Exception as e:
            return f"Could not create parent dir: {parent_dir} = {e}"

    try:
        with open(abs_file_path, "w") as f:
            f.write(content)

        return f"Successfully wrote to {file_path} ({len(content)} characters)"
    except Exception as e:
        print("Error: This error from write_file function.")
        return f"Error: failed to write file {e}"
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file, constrained to the working directory. Creates parent directories if they do not exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },   
        required=["file_path", "content"],
    ),
)