import flask


bot = flask.Blueprint('bot', __name__)

from . import calendar


@bot.route('/', methods=['POST'])
def on_event():
    event = flask.request.get_json()
    if event['type'] == 'ADDED_TO_SPACE' and not event['space']['singleUserBotDm']:
        text = "added to chat!"
    elif event['type'] == 'MESSAGE':
        text = "hiya!"
    else:
        return
    return flask.jsonify({'text': text})
