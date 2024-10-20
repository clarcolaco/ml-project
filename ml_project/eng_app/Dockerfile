FROM python:3.11
WORKDIR ..
COPY /ml_project/eng_app ./eng_app
RUN cd /eng_app
RUN pip install --no-cache-dir -r ./eng_app/requirements.txt
EXPOSE 8501
CMD ["streamlit","run", "./eng_app/app.py"]