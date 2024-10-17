from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='LaTeXMerger',
      version='0.1',
      description='LaTeX Merger merges multiple LaTeX files into one single file',
      long_description='LaTeX Merger is a Python tool that merges multiple LaTeX files into one single file by recursively searching for \input{} commands within the specified LaTeX files. The tool processes a main LaTeX file and its dependencies, combining them into a single output file named [filename]-merged.tex.',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.11',
          'Topic :: Utilities',
      ],
      keywords='LaTex, merge, input',
      url='https://github.com/hhchen1105/LatexMerger',
      author='Hung-Hsuan Chen',
      author_email='hhchen@ncu.edu.tw',
      license='MIT',
      packages=['latexmerger'],
      py_modules=['latexmerger.py'],
      entry_points={
          'console_scripts': [
              'latexmerger=latexmerger:main',
          ],
      },
      install_requires=[
      ],
      include_package_data=True,
      zip_safe=False,
      setup_requires=['pytest-runner'],
      tests_require=[
          'pytest',
      ],
      scripts=[
            'latexmerger/latexmerger.py',
      ],
)
