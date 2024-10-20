FROM python:3.11
WORKDIR ..
COPY /ml_project/pt_app ./pt_app
# RUN cd /pt_app
RUN pip install --no-cache-dir -r ./pt_app/requirements.txt
EXPOSE 8502
CMD ["streamlit","run", "./pt_app/app_pt.py"]