FROM python:3.6.2

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY manage.py ./
COPY lipsumation ./lipsumation
COPY db.sqlite3 ./

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]
