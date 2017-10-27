FROM python:3

RUN git clone https://github.com/wuvt/notecharlie.git /usr/src/app

WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

VOLUME ["/data"]

USER daemon

CMD ["/usr/src/app/phenny", "-c", "/data/default.py"]
