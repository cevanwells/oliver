import flask


bot = flask.Blueprint('bot', __name__)

from . import calendar


@bot.route('/', methods=['POST'])
def on_event():
    event = flask.request.get_json()
    sender = event['message']['sender']['displayName']
    response = ""
    if event['type'] == 'MESSAGE':
        response = f"hey, {sender}!"
    else:
        return
    return flask.jsonify({'text': response})
