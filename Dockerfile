FROM python
COPY . /app
WORKDIR /app

VOLUME /C:/Volumes/ :/app/Volume/
RUN pip install -r requirements.txt

CMD python3 app.py