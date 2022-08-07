#language
FROM python:3.10

WORKDIR /app
COPY requirement.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

CMD [ "python3","discord-template.py" ]
