from docx import Document

class WordService:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_file(self):
        doc = Document(self.filepath)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)
