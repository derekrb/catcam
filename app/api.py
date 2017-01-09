from flask import request, Response
import subprocess

from app import app
import camera

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
    cmd.append(VIDEOS[request.args['video']])
    subprocess.check_call(cmd)

    return 'OK', 200

@app.route('/stream')
def stream():
    return Response(camera.gen(camera.Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
