FROM python:3.7

WORKDIR /garbage_classifier_app

COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt


COPY app.py .
COPY model_weights.h5 .
COPY model.json .
COPY predict.py .
COPY ./static ./static
COPY ./templates ./templates


CMD ["python", "app.py"]