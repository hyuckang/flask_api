from flask import flask, render_template
import json
app = Flask(__name__)

'''
    'http://[ip주소]:[port번호]' 를 요청하면
    hello_sever 함수가 실행되며 응답으로 index.html를 띄워주게 된다.
'''
@app.route('/')
def hello_server():
    return render_template('index.html')


'''
    'http://[ip주소]:[port번호]/hello' 를 요청하면
    응답으로 json을 돌려준다.
'''
@app.route("hello")
def hello():
    return jsonify({'response' : 'world'})
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1234)