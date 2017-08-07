# =====================================================================================================================
#                                                   example docker file
#         objective: provide a light weight linux appliance to run small etl scripts
#             * establish a postgres database. set timezone, configure persistent storage
#             * establish a box that has current a python 2 dist and appropriate odbc drivers
# =====================================================================================================================

# =====================================================================================================================
#  i started with the jenkins base image. its an ubuntu image loaded with the most common default packages relavent here
#  a better option would be to use an alpine dist and individually select appropriate packages.
# =====================================================================================================================

FROM jenkins/jenkins
USER root
RUN apt-get update && apt-get install -y vim \
 && apt-get install -y ssh openssh-client unixodbc-dev

RUN apt-get install -y python python-dev python-pip build-essential \
                        postgresql postgresql-contrib odbc-postgresql

RUN pip install --upgrade pip
RUN pip install sqlalchemy psycopg2 pyodbc pdb


# =====================================================================================================================
# generally i would build a python virtualenv, and install packages into that.
# to keep it simple, were just going to run a single script without a direct bash entrypoint
# =====================================================================================================================

COPY cool_feature.py /app/

# set language and timezone
ENV LANG en_US.utf8
ENV TZ 'America/Los_Angeles'

# configure credential files
COPY scripts/credentials/odbc.ini /etc/odbc.ini
COPY scripts/credentials/odbcinst.ini /etc/odbcinst.ini


USER jenkins






