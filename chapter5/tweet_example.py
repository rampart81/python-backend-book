from flask import Flask, jsonify, request 

app          = Flask(__name__)
app.users    = {}
app.id_count = 1
app.tweets   = []

@app.route('/tweet', methods=['POST'])
def tweet():
    payload = request.json
    user_id = int(payload['id'])
    tweet   = payload['tweet']

    if user_id not in app.users:
        return '유저가 존재 하지 않습니다', 400

    if len(tweet) > 300:
        return '300자를 초과했습니다', 400

    user_id = int(payload['id'])

    app.tweets.append({
        'user_id' : user_id,
        'tweet'   : tweet
    })

    return '', 200
