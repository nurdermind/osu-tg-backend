FROM python:3.11

WORKDIR /src/
RUN mkdir "tmp"

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .
RUN python main.py

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]