FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive

RUN sed -i 's|http://archive.ubuntu.com/ubuntu/|http://azure.archive.ubuntu.com/ubuntu/|g' /etc/apt/sources.list && \
    apt-get update -o Acquire::Retries=5 && \
    apt-get install -y --no-install-recommends python3-fontforge python3-pip poppler-utils && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir pdf2image

WORKDIR /font

COPY  build_font.py build_font.py 

ENTRYPOINT ["python3"]
CMD  ["/font/build_font.py"]
