FROM python:3.9.7

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 3000
