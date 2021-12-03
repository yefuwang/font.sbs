FROM ubuntu:20.04
ENV DEBIAN_FRONTEND noninteractive

RUN apt update && \
    apt install -y python3-fontforge python3-pip poppler-utils

RUN pip3 install pdf2image

WORKDIR /font

COPY  build_font.py build_font.py 

ENTRYPOINT ["python3"]
CMD  ["/font/build_font.py"]

