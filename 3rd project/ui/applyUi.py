import os
import subprocess

def convert_ui_to_py(ui_dir, output_dir):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Recursively search for .ui files in the UI directory
    for root, _, files in os.walk(ui_dir):
        for filename in files:
            if filename.endswith(".ui"):
                # Construct input and output file paths
                input_file = os.path.join(root, filename)
                output_file = os.path.join(output_dir, os.path.relpath(input_file, ui_dir))
                output_file = os.path.splitext(output_file)[0] + "_ui.py"

                # Convert .ui file to .py using pyuic5
                subprocess.run(["pyuic5", input_file, "-o", output_file])
                print(f"Converted {input_file} to {output_file}")

if __name__ == "__main__":
    # Specify UI directory and output directory
    ui_directory = ".\\3rd project\\ui\\"
    output_directory = ".\\3rd project\\ui\\"

    # Convert .ui files to .py
    convert_ui_to_py(ui_directory, output_directory)