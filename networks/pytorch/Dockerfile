FROM ubuntu:20.04

# Initialize Package Manager 
RUN apt update

# Install Python3 & Pip
RUN apt install --yes python3 python3-pip

# Install PyTorch Without CUDA
RUN pip3 install torch==1.7.0+cpu torchvision==0.8.1+cpu torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html --no-cache-dir
