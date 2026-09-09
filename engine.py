import base64
def run_b64(s):
    exec(base64.b64decode(s).decode("utf-8"), globals())
