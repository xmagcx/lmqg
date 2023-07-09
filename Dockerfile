FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim-2023-07-03
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . /app


RUN pip --no-cache-dir install -r requirements.txt && python -m spacy download en_core_web_sm
#RUN python -m spacy download ja_core_news_sm
#RUN python -m spacy download de_core_news_sm
#RUN python -m spacy download es_core_news_sm
#RUN python -m spacy download it_core_news_sm
#RUN python -m spacy download ko_core_news_sm
#RUN python -m spacy download ru_core_news_sm
#RUN python -m spacy download fr_core_news_sm

#ENV PORT 8080
EXPOSE 8080

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080","--timeout-keep-alive","600","--workers","10"]


