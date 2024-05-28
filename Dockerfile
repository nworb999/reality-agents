FROM python:3.9-slim

WORKDIR /usr/src/app

COPY .ssh_id_rsa /root/.ssh/id_rsa
RUN chmod 600 /root/.ssh/id_rsa && \
    echo "Host github.com\n\tStrictHostKeyChecking no\n" >> /root/.ssh/config

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENV NAME World
ENV ENV production

# CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", ":8000", "main:app"]



#CMD ["python", "main.py", "--test"]
CMD ["python", "main.py", "--production"]

