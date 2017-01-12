FROM postgres:9.5

RUN apt-get update && apt-get -y install \
           build-essential git libicu-dev \
           postgresql-server-dev-$PG_MAJOR=$PG_VERSION

RUN mkdir -p /usr/src/musicbrainz-unaccent \
        && git clone https://github.com/metabrainz/postgresql-musicbrainz-unaccent.git \
        && cd postgresql-musicbrainz-unaccent \
        && make \
        && make install

RUN mkdir -p /usr/src/musicbrainz-collate \
        && git clone https://github.com/metabrainz/postgresql-musicbrainz-collate.git \
        && cd postgresql-musicbrainz-collate \
        && make \
        && make install

RUN apt-get purge -y --auto-remove \
        build-essential git postgresql-server-dev-$PG_MAJOR=$PG_VERSION \
        libicu-dev \
        && rm -rf /var/lib/apt/lists/*
