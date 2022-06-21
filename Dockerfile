FROM python:3.7
WORKDIR /
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "tekton_client.py"]