FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /tinker_api

WORKDIR /tinker_api

COPY requirements.txt /tinker_api/

RUN pip install -r requirements.txt

COPY . /tinker_api/

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Tinker.wsgi:application"]
