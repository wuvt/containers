FROM python:3

RUN git clone https://github.com/wuvt/notecharlie.git /usr/src/app

WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

RUN groupadd -r -g 200 bot \
        && useradd -mr -g bot -u 200 bot
USER bot

VOLUME ["/home/bot/.phenny"]

CMD ["/usr/src/app/phenny"]
