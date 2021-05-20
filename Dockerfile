FROM python:3.8

WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY Pipfile Pipfile.lock ./

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --ignore-pipfile

COPY . .
RUN chmod +x run.sh

EXPOSE 8000

CMD ["bash", "run.sh"]