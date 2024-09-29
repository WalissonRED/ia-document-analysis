import openai
from services.config import model_gpt

class GPTService:
    def __init__(self, api_key):
        openai.api_key = api_key

    def get_score(self, prompt, text):
        response = openai.ChatCompletion.create(
            model= model_gpt,
            messages=[
                {"role": "system", "content": "Você é um especialista que avalia projetos com base em requisitos específicos."},
                {"role": "user", "content": f"Avalie o seguinte texto com uma nota de 0 a 10 com base nas seguintes necessidades: {prompt}\n\nTexto: {text}"}
            ]
        )
        
        # Obtém a resposta do modelo
        message = response.choices[0].message['content'].strip()

        # Tenta extrair o score de 0 a 10
        try:
            score = float([s for s in message.split() if s.isdigit()][0])
        except (ValueError, IndexError):
            print(f"Erro ao processar o score. Resposta do modelo: {message}")
            return None

        return score

    def generate_new_file(self, prompt, text):
        response = openai.ChatCompletion.create(
            model= model_gpt,
            messages=[
                {"role": "system", "content": "Você é um especialista que ajuda a reescrever textos de acordo com necessidades específicas."},
                {"role": "user", "content": f"Baseado nas seguintes necessidades: {prompt}, reescreva o seguinte texto: {text}"}
            ]
        )
        new_text = response.choices[0].message['content'].strip()
        return new_text