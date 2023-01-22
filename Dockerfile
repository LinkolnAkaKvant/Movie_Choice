FROM python:3.10

COPY requirements.txt .
RUN python3 -m pip install --no-cache -r requirements.txt

COPY . .

CMD ["sh", "entrypoint.sh"]