from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model/googleModel.pkl', 'rb'))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    open_price = float(request.form['open_price'])
    highest_price = float(request.form['highest_price'])
    lowest_price = float(request.form['lowest_price'])
    volume = int(request.form['volume'])
    print(open_price, highest_price, lowest_price, volume)
    prediction = model.predict([[open_price, highest_price, lowest_price, volume]])
    output = float(prediction[0])
    return render_template("index.html", prediction_text=f'${round(output, 2)}')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3003)
