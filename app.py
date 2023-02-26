from flask import Flask, request, url_for, render_template
from sklearn.preprocessing import StandardScaler
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

app=Flask(__name__)
model=pickle.load(open('model.pkl', 'rb'))
@app.route('/', methods=['GET'])
def home():
   return render_template('index.html')

""" @app.route("/predict",methods=['POST'])
def predict():
    if request.method == 'POST':
        WC = float(request.form['wc'])
        BGR = float(request.form['bgr'])
        BU = float(request.form['bu'])
        SC = float(request.form['sc'])
        PCV = float(request.form['pcv'])
        AL = float(request.form['al'])
        HEMO = float(request.form['hemo'])
        AGE = float(request.form['age'])
        SU = float(request.form['su'])
        HTN = float(request.form['htn'])

        prediction=model.predict([[WC,BGR,BU,SC,PCV,AL,HEMO,AGE,SU,HTN]])

        if prediction==1:
            return render_template('index.html',pred='Patient has Chronic Kidney Disease. ')
        else:
            return render_template('index.html',pred='Patient  is safe Patient doesnot have CKD')
    else:
        return render_template('index.html') """
    
@app.route("/predict",methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    # final_output = StandardScaler.transform(np.array(list(data.values())).reshape(1, -1))
    print(data)
    prediction = model.predict([data])
    if prediction==1:
        return render_template('index.html',pred='Patient has Chronic Kidney Disease. ')
    else:
        return render_template('index.html',pred='Patient  is safe Patient doesnot have CKD')

if __name__=='__main__':
     app.run()