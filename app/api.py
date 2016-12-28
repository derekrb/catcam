from flask import request
import subprocess

from app import app


VIDEOS = {
    'test': '/opt/vc/src/hello_pi/hello_video/test.h264'
}


@app.route('/ping')
def index():
    return 'OK', 200


@app.route('/video')
def video():

    if 'video' not in request.args:
        return 'video param required', 400
    elif request.args['video'] not in VIDEOS:
        return 'unrecognized video', 400

    cmd = ['omxplayer', '-b', '-o', 'hdmi']
    cmd.append(VIDEOS[video])
    subprocess.check_call(cmd)

    return 'OK', 200
