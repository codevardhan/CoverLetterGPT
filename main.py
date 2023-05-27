import openai
import dotenv
import argparse
import os
import docx

from PyPDF2 import PdfReader

config = dotenv.dotenv_values(".env")
openai.api_key = config["OPENAPI_KEY"]


def extract_file_data(file_path):
    extension = os.path.splitext(file_path)[1]
    text = ""
    if extension == ".pdf":
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text()
    elif extension == ".txt":
        with open(file_path) as f:
            text = " ".join(f.readlines())
    elif extension == ".docx":
        doc = docx.Document(file_path)
        text_list = []
        for para in doc.paragraphs:
            text_list.append(para.text)
        text = "\n".join(text_list)

    return text


def __file_type_check(file_path):
    allowed_extensions = [".txt", ".pdf", ".docx"]
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower() in allowed_extensions


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process two document files.")
    parser.add_argument("resume", help="Path to the resume file")
    parser.add_argument("job_desc", help="Path to the job description file")

    args = parser.parse_args()

    resume_path = args.resume
    job_desc_path = args.job_desc

    if not (__file_type_check(resume_path) and __file_type_check(job_desc_path)):
        print("Error: Both files must be in document format (.txt, .pdf, .docx)")
        quit

    resume_details = extract_file_data(resume_path)
    job_description_details = extract_file_data(job_desc_path)

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"""Write a job application cover letter for a candidate with the 
                    following resume details :```{resume_details}```, if the job
                    description is as follows:```{job_description_details}```""",
        max_tokens=2048,
        temperature=0,
    )

    result = response["choices"][0]["text"]
    print(result)
