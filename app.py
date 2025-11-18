from flask import Flask
app = Flask(__name__)

# http://.../ というアクセスが来たら、この関数が実行される
@app.route('/')
def hello_world():
    # 'Hello, Docker! 🐳' という文字をブラウザに返す
    return 'Hello, Docker! 🐳'

if __name__ == '__main__':
    # コンテナの中からアクセスできるように '0.0.0.0' を指定
    app.run(debug=True, host='0.0.0.0', port=5000)