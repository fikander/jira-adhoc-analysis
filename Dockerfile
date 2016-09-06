FROM python:3-slim
MAINTAINER Tomasz Kustrzynski <tomasz.kustzynski@gmail.com>

#
# Install dependencies
#

RUN apt-get update && \
	apt-get install -y build-essential git libfreetype6-dev libxft-dev

WORKDIR /
ADD requirements.txt /
RUN pip3 install -r requirements.txt

#
# Setup sources
#

ADD jupyter_notebook_config.py /root/.jupyter/
ADD tools /src/tools
ENV PYTHONPATH=/src

CMD jupyter notebook
