from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient("mongodb+srv://test:sparta@cluster0.9pyyebx.mongodb.net/Cluster0?retryWrites=true&w=majority")
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/like1', methods=['POST'])
def update_like_cnt1():
    like = db.likes.find_one({'name': '김태웅'})['likes']
    print(like)

    db.likes.update_one({'name':'김태웅'},{'$set':{'likes':like+1}})
    like = db.likes.find_one({'name': '김태웅'})['likes']

    return jsonify({'name': '김태웅', 'like': like})

@app.route('/like1', methods=['GET'])
def get_like_cnt1():
    like = db.likes.find_one({'name': '김태웅'})['likes']
    print(like)

    return jsonify({'name':'김태웅', 'like': like})

@app.route('/like2', methods=['POST'])
def update_like_cnt2():
    like = db.likes.find_one({'name': '김송미'})['likes']
    print(like)

    db.likes.update_one({'name': '김송미'}, {'$set': {'likes': like + 1}})
    like = db.likes.find_one({'name': '김송미'})['likes']

    return jsonify({'name': '김송미', 'like': like})

@app.route('/like2', methods=['GET'])
def get_like_cnt2():
    like = db.likes.find_one({'name': '김송미'})['likes']
    print(like)

    return jsonify({'name':'김송미', 'like': like})

@app.route('/like3', methods=['POST'])
def update_like_cnt3():
    like = db.likes.find_one({'name': '이솔'})['likes']
    print(like)

    db.likes.update_one({'name': '이솔'}, {'$set': {'likes': like + 1}})
    like = db.likes.find_one({'name': '이솔'})['likes']

    return jsonify({'name': '이솔', 'like': like})

@app.route('/like3', methods=['GET'])
def get_like_cnt3():
    like = db.likes.find_one({'name': '이솔'})['likes']
    print(like)

    return jsonify({'name':'이솔', 'like': like})

@app.route('/like4', methods=['POST'])
def update_like_cnt4():
    like = db.likes.find_one({'name': '박찬환'})['likes']
    print(like)

    db.likes.update_one({'name': '박찬환'}, {'$set': {'likes': like + 1}})
    like = db.likes.find_one({'name': '박찬환'})['likes']

    return jsonify({'name': '박찬환', 'like': like})

@app.route('/like4', methods=['GET'])
def get_like_cnt4():
    like = db.likes.find_one({'name': '박찬환'})['likes']
    print(like)

    return jsonify({'name':'박찬환', 'like': like})

@app.route('/like5', methods=['POST'])
def update_like_cnt5():
    like = db.likes.find_one({'name': '홍승엽'})['likes']
    print(like)

    db.likes.update_one({'name': '홍승엽'}, {'$set': {'likes': like + 1}})
    like = db.likes.find_one({'name': '홍승엽'})['likes']

    return jsonify({'name': '홍승엽', 'like': like})

@app.route('/like5', methods=['GET'])
def get_like_cnt5():
    like = db.likes.find_one({'name': '홍승엽'})['likes']
    print(like)

    return jsonify({'name':'홍승엽', 'like': like})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)