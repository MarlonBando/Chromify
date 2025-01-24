FROM python:3.11-slim
EXPOSE 8080

RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt clean && rm -rf /var/lib/apt/lists/*

ENV PYTHON_PATH=/

WORKDIR /src
COPY models/ models/
COPY requirements.txt requirements.txt


RUN pip install dvc
RUN pip install dvc-gs
RUN pip install --upgrade google-cloud
RUN pip install google-cloud-storage
RUN pip install streamlit
RUN pip install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "chromify.api:app", "--server.port=8080", "--server.address=0.0.0.0"]