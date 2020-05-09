FROM ubuntu:latest
LABEL maintainer "super_franc"
RUN apt update --fix-missing -y
RUN apt install -y python3-pip
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["patents_app.py"]

# docker run -it --rm --entrypoint="/bin/bash" -p 5002:5000 -v e:/projects/docker_deploy:/app  passing_args
# docker build -t passing_args .
