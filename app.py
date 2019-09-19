from flask import Flask

app = Flask('zapp')


@app.route('/')
def index():
    return "Check CD with Travis specific keys"


if __name__ == '__main__':
    app.run(port=8000)
