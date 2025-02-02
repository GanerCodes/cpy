FROM python:3.13-slim
WORKDIR /
RUN apt-get update && apt-get install -y git
RUN git clone --depth 1 https://github.com/ganercodes/moon
RUN ./moon/install