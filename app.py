# -*- coding: utf-8 -*-

from flask import Flask,render_template,request
import pickle 

print('Model loading!!!')
with open("emotion_ISEAR_pickle (1).pickle", 'rb') as f:
    loaded_obj = pickle.load(f)
print('MOdel loaded!!!')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ab',methods=['POST'])
def index1():
    data = request.form['text']
    data1 = loaded_obj.predict_proba([data])
    return render_template('index.html',text1=data,ang=data1[0][0]*100+30,dis=data1[0][1]*100+30,fea=data1[0][2]*100+30,
                           gui=data1[0][3]*100+30,joy=data1[0][5]*100+30,sad=data1[0][6]*100+30,sha=data1[0][7]*100+30)

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000)
#
#loaded_obj.predict(['hai hello im sad'])[0]



