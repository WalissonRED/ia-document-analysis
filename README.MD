
IA Document Analysis
Este projeto é uma automação de análise de documentos que usa a API GPT-3.5 (via OpenAI) para avaliar e, se necessário, gerar novos textos com base em requisitos pré-definidos. A aplicação foi projetada para trabalhar com arquivos Word, permitindo que o usuário selecione um arquivo e receba um score sobre o conteúdo. Caso o score seja inferior a 7, um novo texto é gerado com base nos requisitos fornecidos.

Funcionalidades
Carregamento de arquivos Word (.docx).
Avaliação de textos com base em requisitos específicos.
Geração de novos textos se o conteúdo original não atender aos critérios.
Integração com a API GPT-3.5 da OpenAI.
Tecnologias Utilizadas
Python 3.10+
OpenAI API (GPT-3.5)
Tkinter para interface de seleção de arquivos.
python-docx para manipulação de arquivos Word.
dotenv para carregar variáveis de ambiente a partir de um arquivo .env.
Instalação e Configuração
Pré-requisitos
Python 3.10+ instalado.
Acesso à API GPT-3.5 da OpenAI (chave de API).
Passos de Instalação
Clone o repositório para sua máquina local:

bash
Copiar código
git clone https://github.com/WalissonRED/ia-document-analysis.git
cd ia-document-analysis
Crie e ative um ambiente virtual:

bash
Copiar código
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Crie um arquivo .env na raiz do projeto com sua chave de API OpenAI e os prompts necessários:

env
Copiar código
OPENAI_API_KEY=your_openai_api_key
PROMPT_RESUMO="Resumo: Deve ter um título claro e conter no mínimo 15 linhas ou 150 palavras."
PROMPT_INTRODUCAO="Introdução: A introdução precisa ter entre 1 e 2 páginas, sem contar imagens, gráficos ou tabelas."
PROMPT_CORPO="Corpo do Trabalho: Deve ter entre 2 e 3 páginas, excluindo imagens, gráficos ou tabelas."
PROMPT_RESULTADOS_CONCLUSAO="Resultados e Discussão, e Conclusão: Devem ocupar 1 página completa, sem contar imagens, gráficos ou tabelas."
PROMPT_TOTAL="Com base nas seguintes diretrizes para um Projeto Multidisciplinar, ajuste o conteúdo do seu trabalho para atender aos critérios estabelecidos."
Como Executar
Inicie a aplicação:

bash
Copiar código
python main.py
Um diálogo será aberto para você selecionar o arquivo Word a ser analisado.

O sistema vai avaliar o arquivo com base nos requisitos definidos e retornará um score.

Se o score for inferior a 7, a aplicação irá gerar um novo texto com base nas diretrizes e salvar em um novo arquivo.

Estrutura do Projeto
bash
Copiar código
.
├── main.py                # Arquivo principal que orquestra a aplicação
├── services/
│   ├── __init__.py
│   ├── word_service.py     # Classe para manipulação de arquivos Word
│   ├── gpt_service.py      # Classe para integração com a API GPT-3.5
│   ├── config.py           # Configurações e carregamento do .env
├── .env                    # Arquivo de variáveis de ambiente (não incluído no repositório)
├── .gitignore              # Arquivos e diretórios ignorados pelo Git
├── README.md               # Documentação do projeto
├── requirements.txt        # Lista de dependências
Contribuições
Sinta-se à vontade para abrir issues e pull requests se quiser contribuir com melhorias no projeto.

Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

Esse README.md é completo e inclui todos os detalhes necessários para usar, instalar e contribuir para o projeto.
