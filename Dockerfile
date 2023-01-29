FROM python:3.9-alpine3.16
LABEL Name=Sai Project=Softglacier
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV FLASK_APP=app.py
ENV FLASK_DEBUG=FALSE

EXPOSE 3000
CMD [ "python", "app.py" ]