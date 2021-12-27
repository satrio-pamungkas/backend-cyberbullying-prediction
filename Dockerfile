# Install Python
FROM python:3.8-bullseye

RUN python3 -m venv /opt/venv

# Copy directory and file
COPY ./app.py /app/app.py 
COPY ./prediction.py /app/prediction.py
COPY ./requirements.txt /app/requirements.txt
COPY notebooks /app/notebooks 
COPY model /app/model 
COPY dataset /app/dataset 

RUN . /opt/venv/bin/activate && pip install -r /app/requirements.txt

WORKDIR /app 

ENV PORT=8000
EXPOSE 8000

CMD . ../opt/venv/bin/activate && exec python app.py





