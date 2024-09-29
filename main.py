import tkinter as tk
from tkinter import filedialog
from services.word_service import WordService
from services.gpt_service import GPTService
from services.config import api_key_gpt, prompt_requirements

def select_file():
    root = tk.Tk()
    root.withdraw()
    filepath = filedialog.askopenfilename(
        title="Selecione o arquivo Word",
        filetypes=(("Arquivos Word", "*.docx"), ("Todos os arquivos", "*.*"))
    )
    return filepath

file_path = select_file()

if file_path:
    word_service = WordService(file_path)
    gpt_service = GPTService(api_key_gpt)
    texto = word_service.read_file()

    prompt_needs = prompt_requirements

    score = gpt_service.get_score(prompt_needs, texto)

    print(f"Score do texto: {score}")

    if score is not None and score < 7:
        print("O texto não atende às necessidades. Gerando um novo texto...")
        novo_texto = gpt_service.generate_new_file(prompt_needs, texto)

        with open("novo_arquivo.txt", "w") as f:
            f.write(novo_texto)
        print("Novo arquivo gerado com sucesso.")
    else:
        print("O texto atende às necessidades.")
else:
    print("Nenhum arquivo selecionado.")
