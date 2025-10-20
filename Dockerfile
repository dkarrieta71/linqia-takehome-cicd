# Use a slim CPython base
FROM python:3.12-slim

# Avoid prompts & keep image small
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# System deps (if needed). Kept minimal here.
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Copy only what we need (adjust paths if your package layout differs)
COPY . .

# Install runtime requirements if present
# (Project is tiny; if you have requirements.txt, uncomment)
# RUN pip install -r requirements.txt

# Default entrypoint is python; we'll pass module/args at runtime
ENTRYPOINT ["python"]
