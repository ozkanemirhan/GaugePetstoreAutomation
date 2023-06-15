FROM python:3.10

WORKDIR /app

RUN apt-key adv --keyserver hkp://pool.sks-keyservers.net --recv-keys 023EDB0B \
  && echo deb https://dl.bintray.com/gauge/gauge-deb stable main | tee -a /etc/apt/sources.list \
  && apt-get update \
  && apt-get install gauge -y --no-install-recommends \
  && rm -rf /var/lib/apt/lists/*

RUN gauge install python
RUN gauge install html-report
RUN gauge install screenshot
RUN gauge install flash
RUN gauge install spectacle
RUN gauge install xml-report --log-level=debug

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
RUN pip install --upgrade pip

COPY . /app

ENTRYPOINT [ "gauge", "run" ]