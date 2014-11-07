import hglib
from flask import current_app

# Find the stack on which we want to store the database connection.
# Starting with Flask 0.9, the _app_ctx_stack is the correct one,
# before that we need to use the _request_ctx_stack.
try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack


class Mercurial(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('MERCURIAL_REPOPATH', '/tmp')

    def open_client(self):
        return hglib.open(current_app.config['MERCURIAL_REPOPATH'])

    @property
    def client(self):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'hg_client'):
                ctx.hg_client = self.open_client()
            return ctx.hg_client

    def commits(self, reverse=False):
        if reverse:
            return self.client.log(':')
        else:
            return self.client.log()

    def commits_for_path(self, path, reverse=False):
        if reverse:
            return self.client.log(':', files=[path])
        else:
            return self.client.log(files=[path])

