# Use a imagem base oficial do Python
FROM python:3.11-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo de requisitos primeiro (melhora o cache do Docker)
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o conteúdo da aplicação
COPY . .

# Exponha a porta (o Render/Koyeb costuma usar a variável $PORT)
EXPOSE 80

# Comando de inicialização ajustado para produção
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]