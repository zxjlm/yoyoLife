"""
    @author: harumonia
    :@url: http://harumonia.top
    :copyright: © 2020 harumonia<zxjlm233@gmail.com>
    :@site:
    :@datetime: 2020/6/21 9:27
    :@software: PyCharm
    :@description: None
"""

from application import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
