FROM ubuntu:20.04

# Initialize Package Manager 
RUN apt update

# Install Python3 & Pip
RUN apt install --yes python3 python3-pip

# Install Dependencies
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt