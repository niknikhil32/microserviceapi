FROM python:alpine3.9 
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt 
EXPOSE 7000 
ENTRYPOINT [ "python" ] 
CMD [ "app.py" ] 