FROM python:3.7

# RUN apk add --no-cache python3-dev py3-pip \
# && pip3 install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["library/run.py", "library/test_api.py"]

EXPOSE 5000
