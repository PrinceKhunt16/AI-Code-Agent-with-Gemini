import os
from google.genai import types 

def create_folder(working_directory, folder_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_folder_path = os.path.abspath(os.path.join(working_directory, folder_path))

    if not abs_folder_path.startswith(abs_working_dir):
        return f"Error: {folder_path} is not in the directory."

    if os.path.exists(abs_folder_path):
        return f"Error: {folder_path} already exists."

    try:
        os.makedirs(abs_folder_path, exist_ok=True)
        return f"Successfully created folder {folder_path}"
    except Exception as e:
        print("Error: This error is from create_folder.py")
        return f"Error: failed to create folder {e}"

schema_create_folder = types.FunctionDeclaration(
    name="create_folder",
    description="Creates a specified folder, constrained to the working directory. Creates parent directories if they do not exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "folder_path": types.Schema(
                type=types.Type.STRING,
            ), 
        },
        required=["folder_path"],
    ),
)