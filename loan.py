from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)  # Correct usage


with open(r'C:\Users\krishna devda\OneDrive\Desktop\Loan_prediction_model\model\loan_prediction.pkl','rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index5.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_features = [int(request.form['Gender']),
                      int(request.form['Married']),
                      int(request.form['Education']),
                      float(request.form['ApplicantIncome']),
                      float(request.form['CoapplicantIncome']),
                      float(request.form['LoanAmount']),
                      float(request.form['Loan_Amount_Term']),
                      int(request.form['Credit_History']),
                      int(request.form['Property_Area_Rural']),
                      int(request.form['Property_Area_Semiurban']),
                      int(request.form['Property_Area_Urban'])]

    input_array = np.array([input_features])
    
    prediction = model.predict(input_array)

    if prediction[0] == 1:
        result = "Your lone will be approved"
    else:
        result = "Your loan will not be approved"
                         
    return render_template('index5.html', prediction_result=result)

if __name__ == '__main__': 
    app.run(debug=True) 
