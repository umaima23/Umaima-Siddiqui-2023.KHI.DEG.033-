FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

VOLUME /app/data  # Attach a Docker volume to store the todo.json file

CMD ["python", "main.py"]
