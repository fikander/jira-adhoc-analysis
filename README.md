# What it is
This is a tool for ad hoc analysis of JIRA issues using Python data analysis libraries (numpy, [pandas](http://pandas.pydata.org/), seaborn).
It's packaged as a [Docker](http://docker.com) image, which makes it easy to run locally on your machine or deploy to a server within your network (note there's not authentication mechanism enabled, so web interface and data is accessible to everyone without logging in).
It is not really meant to be used by multiple users at the moment, so deployment on local machine for personal use is recommended (see Installation below).

The main user interface for analysis is [Jupyter](http://jupyter.org) notebook.
Packaged in the image is [jira-cycle-extract](https://github.com/fikander/jira-cycle-extract) library which performs basic analysis of JIRA issues. Configuration of JIRA query, columns and data to be extracted from issues is supplied as YAML text.

# Installation
The only prerequisite to installation is Docker. Install [Docker for your platform](http://docker.com) and make sure `docker` and `docker-compose` are working before continuing.

    git clone https://github.com/fikander/jira-adhoc-analysis.git
    cd jira-adhoc-analysis

To configure JIRA connection, create .env file containing environment variable definition with JIRA domain, username and password (optionally 'token' which is base64 encoded username:password string).
There's example `.env-sample` file which you can copy and modify with your values.

    cp .env-sample .env

Next, launch the server:

    docker-compose up -d

This will take time for the first time as the image (around 1GB at the moment) needs to be pulled from Docker hub:

    => docker-compose up
    Creating network "jiraadhocanalysis_default" with the default driver
    Pulling server (fikander/jiraadhocanalysis_server:latest)...
    latest: Pulling from fikander/jiraadhocanalysis_server
    357ea8c3d80b: Downloading [==================>                                ] 19.39 MB/51.37 MB
    57aad21b9e0f: Download complete
    15554fdf9e92: Downloading [==============================================>    ] 19.43 MB/20.8 MB
    bcf0d5f75458: Download complete
    5b5fbf431acf: Downloading [==>                                                ] 6.978 MB/124.6 MB
    c41dfae30533: Waiting
    a61b46d690d8: Waiting
    4c91e3518d46: Waiting
    9c719d94c318: Waiting

To shut the server down once you're done:

    docker-compose down

Note, that if you change values in `.env`, you need to restart the server with `docker-compose restart` for changes to take effect.

# Usage
`jira-adhoc-analysis` Docker container exposes Jupyter notebook at http://localhost:8888. Navigate there for Jupyter UI, where the most interesting stuff happens:

![Jupyter UI](/images/jupyter_ui.png)

Check [sample notebook](http://localhost:8888/notebooks/sample.ipynb) for ideas on what and how can be analysed.

Copy sample notebook to customise it.

![Jupyter UI](/images/jupyter_copy.png)

New notebooks will be saved in `notebook` subfolder thanks to Docker volume mapping set up in `docker-compose.yml` used by `docker-compose` call.

## Configuration
To configure for your own project, change `config_yaml` variable and set it up according to [instructions for jira-cycle-extract](https://github.com/fikander/jira-cycle-extract).

![Jupyter UI](/images/jupyter_config.png)

Authentication for your JIRA domain can be accomplished by either editing `.env` file (as described above) or editing `connection` dictionary in `config_yaml` variable, e.g.

    connection:
      domain: http://MY_JIRA_DOMAIN
      username: USERNAME
      password: PASSWORD

You can also specify domain only, like so:

    connection:
      domain: http://MY_JIRA_DOMAIN

in which case you'll be prompted to enter username and password as notebook is being evaluated.

## Executing calculations

Once you've copied the notebook and configured it, execute notebook with Cell -> Run All.

# Advanced Usage
You can open a terminal on the Jupyter server using:

    cd jira-adhoc-analysis
    docker-compose exec server /bin/bash

From there, you can use iPython to execute arbitrary code using pandas, jira-cycle-extract and other installed modules.

# TODO

  - continuous integration
  - Makefile
  - more examples of analysis
  - simplify notebooks by pulling code to tools Python scripts
