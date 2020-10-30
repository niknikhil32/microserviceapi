FROM python:alpine3.9 
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt 
EXPOSE 9000 
ENTRYPOINT [ "python" ] 
CMD [ "app.py" ] 