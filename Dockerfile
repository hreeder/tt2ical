FROM python:3.7

WORKDIR /usr/src/app
EXPOSE 5000

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./

CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "tt2cal:app" ]