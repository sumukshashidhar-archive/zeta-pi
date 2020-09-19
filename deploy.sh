cd server;
pip3 install gunicorn; pip install gunicorn
gunicorn --bind 0.0.0.0:80 wsgi:app; 

