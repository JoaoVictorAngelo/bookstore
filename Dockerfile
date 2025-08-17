# Imagem base
FROM python:3.12.1-slim

# Variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # Diz ao Poetry para instalar dependências no ambiente do sistema, não em um .venv
    POETRY_VIRTUALENVS_CREATE=false

# Instala dependências do sistema e o Poetry
RUN apt-get update \
    && apt-get install --no-install-recommends -y build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install poetry

# Define o diretório de trabalho para a aplicação
WORKDIR /app

# Copia apenas os arquivos de dependência primeiro para usar o cache
COPY poetry.lock pyproject.toml ./

# Instala as dependências
RUN poetry install --no-root --only main

# Copia o resto do código da aplicação
COPY . .

# Expõe a porta
EXPOSE 8000

# Roda o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]