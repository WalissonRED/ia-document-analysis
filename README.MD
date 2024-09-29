# IA Document Analysis

Este projeto é uma automação de análise de documentos que usa a API GPT-3.5 (via OpenAI) para avaliar e, se necessário, gerar novos textos com base em requisitos pré-definidos. A aplicação foi projetada para trabalhar com arquivos Word, permitindo que o usuário selecione um arquivo e receba um score sobre o conteúdo. Caso o score seja inferior a 7, um novo texto é gerado com base nos requisitos fornecidos.

## Funcionalidades

- Carregamento de arquivos Word (.docx).
- Avaliação de textos com base em requisitos específicos.
- Geração de novos textos se o conteúdo original não atender aos critérios.
- Integração com a API GPT-3.5 da OpenAI.

## Tecnologias Utilizadas

- **Python 3.10+**
- **OpenAI API (GPT-3.5)**
- **Tkinter** para interface de seleção de arquivos.
- **python-docx** para manipulação de arquivos Word.
- **dotenv** para carregar variáveis de ambiente a partir de um arquivo `.env`.

## Instalação e Configuração

### Pré-requisitos

- **Python 3.10+** instalado.
- Acesso à **API GPT-3.5** da OpenAI (chave de API).

### Passos de Instalação

1. Clone o repositório para sua máquina local:

   ```bash
   git clone https://github.com/WalissonRED/ia-document-analysis.git
   cd ia-document-analysis
