FROM python:3
LABEL maintainer "WUVT IT <it+dockerfiles@wuvt.vt.edu>"

RUN pip install --no-cache-dir requests==2.18.4
COPY prune_logs.py /usr/src/app/
CMD ["python", "/usr/src/app/prune_logs.py"]
