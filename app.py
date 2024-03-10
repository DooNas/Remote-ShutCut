from flask import Flask
import pyautogui


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()


@app.route('/CAM')
def not_cam():
    pyautogui.press('z')
    return '<h2>CAM MODE ON</h2>'

@app.route('/ALL')
def not_all():
    pyautogui.press('x')
    return '<h2>ALL MODE ON</h2>'