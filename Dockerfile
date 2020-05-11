FROM ubuntu:latest
LABEL maintainer "super_franc"
RUN apt update --fix-missing -y
RUN apt install -y python3-pip
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
#ENTRYPOINT ["/bin/bash"]
#CMD ["patents_app.py"]
CMD ["gunicorn" , "--bind", "0.0.0.0:4646", "--workers", "2", "--threads", "4", "--worker-class", "gthread", "--chdir", "/app", "wsgi:app"]
EXPOSE 4646

#https://pythonspeed.com/articles/gunicorn-in-docker/
# docker run -it --rm --entrypoint="/bin/bash" -p 5002:5000 -v e:/projects/docker_deploy:/app  passing_args
# docker build -t passing_args .
