FROM python:3.9.16-slim

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["predict.py", "churn-predict-model.bin", "./"]

EXPOSE 9696

#ENTRYPOINT {"gunicorn", "--bind=0.0.0.0:9696", "predict:app"}

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "predict:app"]

#To build the docker file
# docker build -t zcml-test .

# To run the docker file
# docker run -it --rm zcml-test

#To run the docker file through bash
#docker run -it --rm --entrypoint=bash zcml-test:latest

# To map my system port with docker port
# docker run -it --rm -p 9696:9696 zcml-test    