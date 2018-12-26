# start from base
FROM ubuntu:latest

# install system-wide deps for python and node
RUN apt-get -yqq update
RUN apt-get -yqq install python-pip python-dev curl gnupg
#RUN curl -sL https://deb.nodesource.com/setup_8.x | bash
#RUN apt-get install -yq nodejs

# copy our application code
ADD flaskapp /opt/flask-app
WORKDIR /opt/flask-app

# fetch app specific deps
#RUN npm install
#RUN npm run build
RUN pip install -r requirements.txt


# expose port
EXPOSE 5000

# Add environment vars
ENV FLASK_PORT=5000
ENV FLASK_DEBUG=True

# start app
CMD [ "python", "./app.py" ]