FROM python:3.7.3
MAINTAINER Frédéric Pinaud, fpinaud17@gmail.com
COPY . /Fruits
WORKDIR /Fruits
RUN pip install -r requirements.txt
RUN pip install flask-mysql
ENTRYPOINT ["python"]
CMD ["app.py"]