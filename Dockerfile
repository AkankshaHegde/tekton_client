FROM python:3.7
RUN mkdir /tekton-applicatn
WORKDIR /tekton-applicatn/
COPY . /tekton-applicatn/
RUN pip install -r requirements.txt
CMD ["python", "/tekton-applicatn/tekton_client.py"]