from tika import parser

def extract_text(file_path):
    parsed_pdf = parser.from_file(file_path)
    return parsed_pdf['content']