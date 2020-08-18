'''
    @author: harumonia
    :@url: http://harumonia.top
    :copyright: © 2020 harumonia<zxjlm233@gmail.com>
    :@site: 
    :@datetime: 2020/6/21 16:20
    :@software: PyCharm
    :@description: None
'''


import multiprocessing

# debug = True
# threads = 2
worker_connections = 200
loglevel = 'info'
bind = "0.0.0.0:5000"
pidfile = '/logs/gunicorn/gunicorn.pid'
accesslog = '/logs/gunicorn/gunicorn_acess.log'
errorlog = '/logs/gunicorn/gunicorn_error.log'
daemon = True

# 启动的进程数
workers = multiprocessing.cpu_count()
worker_class = 'sync'
x_forwarded_for_header = 'X-FORWARDED-FOR'
