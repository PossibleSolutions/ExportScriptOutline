import nbformat
import re
import os

# Define regular expression pattern to match comments
#'r'^\s*#' matches any line that starts with zero or more whitespace characters followed by the comment symbol "#"
comment_pattern = re.compile(r'^\s*#')

# Get the absolute path and directory name of the input file
input_path = os.path.abspath(r"YOURDATAPATH")
input_dirname = os.path.dirname(input_path)

# Construct the output file path in the same directory as the input file
output_path = os.path.join(input_dirname, 'ScriptComments_summary.txt')

# Open input file and output text file
with open(input_path, 'r', encoding='utf-8') as input_file, open(output_path, 'w') as output_file:
    # If input file is a Python script
    if input_file.name.endswith('.py'):
        # Loop through each line in the Python script
        for line in input_file:
            # If the line matches the comment pattern
            if comment_pattern.match(line):
                # Write the line to the output file
                output_file.write(line)
    # If input file is an IPython Notebook
    elif input_file.name.endswith('.ipynb'):
        # Parse the notebook file
        notebook = nbformat.read(input_file, as_version=nbformat.NO_CONVERT)

        # Loop through each cell in the notebook
        for cell in notebook.cells:
            # If the cell is a code cell
            if cell.cell_type == 'code':
                # Loop through each line in the cell source
                for line in cell.source.splitlines():
                    # If the line matches the comment pattern
                    if comment_pattern.match(line):
                        # Write the line to the output file
                        output_file.write(line+'\n')
            # If the cell is a markdown cell
            elif cell.cell_type == 'markdown':
                # Write the entire markdown cell as a comment with bold text
                output_file.write('***'+cell.source.strip()+'***\n')

print("file was saved to:", output_path)
