FROM python:3.7
COPY . /app
RUN pip install tkcalendar
CMD python /app/myCAL.py
