# What it is
This is a tool for ad hoc analysis of JIRA issues using Python data analysis libraries (numpy, [pandas](http://pandas.pydata.org/), seaborn).
It's packaged as a [Docker](http://docker.com) image, which makes it easy to run locally on your machine or deploy to a server within your network (note there's not authentication mechanism enabled, so web interface and data is accessible to everyone without logging in).
It is not really meant to be used by multiple users at the moment, so deployment on local machine for personal use is recommended (see Installation below).

The main user interface for analysis is [Jupyter](http://jupyter.org) notebook.
Packaged in the image is [jira-cycle-extract](https://github.com/fikander/jira-cycle-extract) library which performs basic analysis of JIRA issues. Configuration of JIRA query, columns and data to be extracted from issues is supplied as YAML text.

# Installation
The only prerequisite to installation is Docker. Install [Docker for your platform](docker.com) and make sure `docker` and `docker-compose` are working before continuing.

    git clone https://github.com/fikander/jira-adhoc-analysis.git
    cd jira-adhoc-analysis

To configure JIRA connection, create .env file containing environment variable definition with JIRA domain, username and password (optionally 'token' which is base64 encoded username:password string).
There's example `.env-sample` file which you can copy and modify.

    cp .env-sample .env

Next, launch the server:

    docker-compose up

# Usage
`jira-adhoc-analysis` Docker container exposes Jupyter notebook at http://localhost:8888.


# Advanced Usage
You can open a terminal on the Jupyter server using

    docker-compose -f docker-compose.yml exec server /bin/bash

From there, you can use iPython to execute the same
