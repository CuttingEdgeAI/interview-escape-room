FROM ubuntu:22.10

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    python3

WORKDIR /root/ier

COPY behind_the_scenes.py .
COPY start.py .

CMD ["./start.py"]