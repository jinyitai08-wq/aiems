import signal
import os

bind = "0.0.0.0:5000"
workers = 1
threads = 4
timeout = 120
keepalive = 5
worker_class = "gthread"
accesslog = "-"
errorlog = "-"
loglevel = "info"
preload_app = True

def on_starting(server):
    signal.signal(signal.SIGWINCH, signal.SIG_IGN)

def post_fork(server, worker):
    signal.signal(signal.SIGWINCH, signal.SIG_IGN)
