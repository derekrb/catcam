import subprocess

from app import app


@app.route('/ping')
def index():
    return 'OK', 200


@app.route('/video')
def video():
    cmd = ['omxplayer', '-b', '-o', 'hdmi', '/opt/vc/src/hello_pi/hello_video/test.h264']
    subprocess.check_call(cmd)
    return 'OK', 200
