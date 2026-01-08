from celery import Celery

app = Celery(
    'addTask',
    broker='memory://',
    backend='cache+memory://'
)

@app.task
def add(x, y):
    return x + y
