FROM python:3-alpine
ADD fucking-great-advice.py /
RUN pip3 install python-telegram-bot requests
CMD [ "python3", "/fucking-great-advice.py" ]
