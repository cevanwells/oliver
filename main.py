import os

import oliver


app = oliver.create_app(os.getenv('FLASK_CONFIG') or 'default')
