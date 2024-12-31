# LaTeX Merger

**LaTeX Merger** is a Python tool that merges multiple LaTeX files into one single file by recursively searching for `\input{}` commands within the specified LaTeX files. The tool processes a main LaTeX file and its dependencies, combining them into a single output file named `[filename]-merged.tex`.

## Features

- Recursively parses LaTeX files for the `\input{}` command.
- Merges all referenced files into one consolidated LaTeX file.
- Helps simplify large LaTeX projects by merging separate files into one document.
- Easy to use and fully open source.

## Installation

You can install the LaTeX Merger tool using `pip` by cloning the repository and running the following commands:

```bash
git clone git@github.com:hhchen1105/LatexMerger.git
cd LatexMerger
pip install .
```

## Usage

To use the tool, simply run the following command, pointing to the main LaTeX file:

```bash
latexmerger.py [your-latex-file].tex
```

This will generate a file called `[your-latex-file]-merged.tex`, which will contain the content of the main file and all the files included via the `\input{}` command.
