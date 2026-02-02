FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir requests pytz

COPY vt_cap_to_atom.py .

EXPOSE 8000

CMD ["python", "-u", "vt_cap_to_atom.py"]
