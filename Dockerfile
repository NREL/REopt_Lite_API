FROM python:3.6

ENV SRC_DIR=/opt/reopt/reo/src

# Copy all code
ENV PYTHONDONTWRITEBYTECODE 1
COPY . /opt/reopt

# Install python packages
WORKDIR /opt/reopt
RUN ["pip", "install", "-r", "requirements.txt"]

EXPOSE 8000
ENTRYPOINT ["/bin/bash", "-c"]