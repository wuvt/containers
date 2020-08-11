FROM python:3
LABEL maintainer "WUVT IT <it+dockerfiles@wuvt.vt.edu>"

RUN pip install --no-cache-dir elastalert==0.2.4
CMD ["elastalert", "--config", "/opt/config/config.yaml"]
