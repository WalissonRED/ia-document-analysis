import os
import dotenv

dotenv.load_dotenv()

api_key_gpt = os.getenv("OPENAI_API_KEY")
resumo = os.getenv("PROMPT_RESUMO")
introducao = os.getenv("PROMPT_INTRODUCAO")
corpo = os.getenv("PROMPT_CORPO")
resultados_conclusao = os.getenv("PROMPT_RESULTADOS_CONCLUSAO")
prompt_total = os.getenv("PROMPT_TOTAL")
model_gpt = os.getenv("MODEL_GPT")

prompt_requirements = f"{prompt_total}\n\n{resumo}\n{introducao}\n{corpo}\n{resultados_conclusao}"
