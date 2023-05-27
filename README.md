# CoverLetterGPT

This repository contains a simple Python script that utilizes the power of the GPT (Generative Pre-trained Transformer) model to generate a cover letter for a job application. The script takes a resume and a job description in PDF, docx or txt formats as input and generates a tailored cover letter as output.

## Features

- Automatically generates cover letters for job applications
- Utilizes GPT-3.5 model for natural language generation
- Tailors the cover letter based on the provided resume and job description
- Easy to use command-line interface


## Installation

Clone this repository to your local machine:

```bash
git clone git@github.com:codevardhan/CoverLetterGPT.git
```
Navigate to the project directory:

```bash
cd gpt-cover-letter-generator
```
Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage


Run the following command to generate the cover letter:

```bash
python main.py College_Resume.pdf job_description.txt
```

Replace resume.pdf with the path to your resume file, and job_description.txt with the path to your job description file.

The generated cover letter will be displayed in the console output.

## License
This project is licensed under the MIT License.

## Acknowledgments

This script was inspired by the power of GPT models for natural language generation. Special thanks to OpenAI for their incredible work on the GPT-3.5 model.

If you have any suggestions, improvements, or bug reports, please feel free to create an issue or submit a pull request.

Note: This script utilizes the GPT-3.5 model, which requires API access. Make sure to configure the script accordingly before usage.
