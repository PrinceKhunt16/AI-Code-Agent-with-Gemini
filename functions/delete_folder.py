import os
from google.genai import types 

def delete_folder(working_directory, folder_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_folder_path = os.path.abspath(os.path.join(working_directory, folder_path))

    if not abs_folder_path.startswith(abs_working_dir):
        return f"Error: {folder_path} is not in the directory."

    if not os.path.exists(abs_folder_path):
        return f"Error: {folder_path} does not exist."

    if not os.path.isdir(abs_folder_path):
        return f"Error: {folder_path} is not a folder."

    try:
        os.rmdir(abs_folder_path)
        return f"Successfully deleted folder {folder_path}"
    except Exception as e:
        print("Error: This error from delete_folder function.")
        return f"Error: failed to delete folder {e}"

schema_delete_folder = types.FunctionDeclaration(
    name="delete_folder",
    description="Deletes a specified folder, constrained to the working directory.",
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