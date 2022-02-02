from .app import app


@app.task(bind=True)
def debug_task(self):
    return True


@app.task(bind=True)
def mul(self, x, y):
    return x * y
