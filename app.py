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
    data1 = list(data1[0])
    data1[data1.index(max(data1))] +=0.5
    return render_template('index.html',text1=data,ang=data1[0]*100,dis=data1[1]*100,fea=data1[2]*100,
                           gui=data1[3]*100,joy=data1[5]*100,sad=data1[6]*100,sha=data1[7]*100)

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000, debug=True)
#
#loaded_obj.predict(['hai hello im sad'])[0]



