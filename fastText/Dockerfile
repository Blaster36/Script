# Create image based on Ubuntu
# docker build -t ubuntu:20.04-ft .
FROM ubuntu:20.04

# How to install Python 3.9 on Ubuntu 22.04 from source
WORKDIR /opt/
RUN apt update && apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
RUN wget https://www.python.org/ftp/python/3.9.7/Python-3.9.7.tgz && tar -xvf Python-3.9.7.tgz
RUN Python-3.9.7/configure --enable-optimizations && make && make altinstall
RUN rm -rf Python-3.9.7.tgz && rm -rf Python-3.9.7/
RUN python3.9 -m pip install pip -U

# How to Install fastText on Ubuntu 22.04 using APT
WORKDIR /opt/
RUN apt -y install git make gcc g++
RUN git clone https://github.com/facebookresearch/fastText.git
RUN python3.9 -m pip install pybind11
WORKDIR /opt/fastText/
RUN python3.9 -m pip install .
RUN python3.9 -m pip install gensim
RUN mkdir /home/jovyan
WORKDIR /home/jovyan
RUN cd .. && rm -rf /opt/fastText/

