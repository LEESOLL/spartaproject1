from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient("mongodb+srv://test:sparta@cluster0.ky4ufb9.mongodb.net/?retryWrites=true&w=majority")
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/guest", methods=["POST"])
def guest_post():
    name_receive = request.form["name_give"]
    comment_receive = request.form["comment_give"]

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }

    db.guest.insert_one(doc)
    return jsonify({'msg': '앙응원띠!'})


@app.route("/guest", methods=["GET"])
def guest_get():
    comment_list = list(db.guest.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})

@app.route("/like", methods=["POST"])
def like_count():
    like_receive = request.form["like_give"]

    like_list = list(db.like.find({}, {'_id': False}))
    count = len(like_list) + 1

    doc = {
        'likes' : count
    }
    db.like.insert_one(doc)
    return jsonify({'msg': '❤좋아요 좋아요❤'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)