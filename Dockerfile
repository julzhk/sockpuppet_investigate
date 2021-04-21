FROM python:3.7
ENV PYTHONUNBUFFERED 1

ADD . /run
WORKDIR /run

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
EXPOSE 8000
