FROM ubuntu:20.04

RUN apt update && \
    apt install -y python3-fontforge

WORKDIR /font

COPY  build_font.py build_font.py 

ENTRYPOINT ["python3"]
CMD  ["/font/build_font.py"]

