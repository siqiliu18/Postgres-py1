FROM python:3.9

WORKDIR /app

# COPY app/requirement.txt ./

# RUN pip install -r requirement.txt
RUN pip install psycopg2

COPY app/test.py /app

CMD ["python", "test.py"]