#!/usr/bin/env python

import sys
import os

def read_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()

def dry_run(filename):
    folder, filename_only = os.path.split(filename)
    lines = read_file(filename)
    missing_files = []
    
    for line in lines:
        if line.strip().startswith(r'\input{'):
            input_filename = os.path.join(folder, line.strip()[7:-1] + '.tex')
            if not os.path.exists(input_filename):
                missing_files.append(input_filename)
    
    if missing_files:
        print("The following input files are missing:")
        for file in missing_files:
            print(file)
        return False
    else:
        print("All input files are present.")
        return True

def merge_latex(filename):
    folder, filename_only = os.path.split(filename)
    lines = read_file(filename)
    merged_content = []
    
    for line in lines:
        if line.strip().startswith(r'\input{'):
            input_filename = os.path.join(folder, line.strip()[7:-1] + '.tex')
            merged_content.extend(read_file(input_filename))
            merged_content.append('\n') # add a newline to prevent previous line ends with a comment
        else:
            merged_content.append(line)
    
    output_filename = f"{os.path.splitext(filename)[0]}-merged.tex"
    with open(output_filename, 'w') as output_file:
        output_file.writelines(merged_content)
    
    print(f"Merged content written to {output_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python merge_latex.py <filename.tex>")
        sys.exit(1)
    if not os.path.exists(sys.argv[1]):
        print(f"Error: {sys.argv[1]} does not exist.")
        sys.exit(1)
    if not dry_run(sys.argv[1]):
        sys.exit(1)
    merge_latex(sys.argv[1])
