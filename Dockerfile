FROM apache/superset:4.1.1
USER root
WORKDIR /app
COPY superset_config.py /app/superset_config.py
COPY requirements.txt /app/
RUN pip install -r requirements.txt
ENV FLASK_APP=superset
ENV SUPERSET_CONFIG_PATH=/app/superset_config.py
RUN superset db upgrade
RUN superset fab create-admin --username admin --firstname Superset --lastname Admin --email admin@superset.com --password admin
RUN superset load_examples
RUN superset init
CMD [ "superset", "run", "-p", "8088", "--with-threads", "--reload", "--debugger" ]