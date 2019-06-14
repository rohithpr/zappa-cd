from flask import Flask

app = Flask('zapp')


@app.route('/')
def index():
    return "hi from zappa!"


if __name__ == '__main__':
    app.run(port=8000)
