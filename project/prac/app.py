from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

# 
# 통상적으로 app.py를 가장 먼저 돌린다/ jsonify JSON화 해줌

@app.route('/') # 도메인에 접속했을때 http://localhost:5000/
def home():
   return render_template('index.html') # templates 폴더안에있는 index.html을 가져옴. 더 하위폴더의 경우 폴더 경로까지 입력해주어야함

@app.route('/mypage') #http://localhost:5000/mypage
def mypage():  
   return 'This is My Page!'

# URL + method (post/get)은 다른것

## API 역할을 하는 부분
@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

# get은 url에 ? 붙여서 가져오기에 args는 URL을 가져오겠다 / localhost:5000/test?title_give=봄날은간다
# @app.route('/test', methods=['GET','POST']) GET,POST 둘다 가져오기 /    title_receive = request.args.get('title_give') or request.form['title_give']


@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give')
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)
   # 브라우저는 localhost로 접속, 0.0.0.0 모든 포트로부터 받겠다

# 딕셔너리는 키값의 순서는 보장안됨 (기본적으로 알파벳순) / 리스트는 순서중요

