FROM python:3
RUN pip install --no-cache-dir requests==2.18.4
COPY prune_logs.py /usr/src/app/
CMD ["python", "/usr/src/app/prune_logs.py"]
