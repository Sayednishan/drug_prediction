'''importing Flask and other modules'''
from flask import Flask, request, render_template
from joblib import load

app = Flask(__name__)

# load the model
model = load("models/model_v1.joblib")


@app.route('/', methods=["GET", "POST"])
def prediction():
    '''
    This will get data from html form and will do prediction.

    Returns
    -------
    html
        html code for render
    '''
    form_items = ['Age','Sex','BP','Cholesterol','Na_to_K']
    d = {0:'DrugY', 1: 'DrugB', 2:'DrugA', 3:'DrugC', 4:'DrugX'}
    data = []
    pred = None

    if request.method == "POST":
        # getting input with name = fname in HTML form
        for item in form_items:
            try:
                temp = request.form.get(item)
                temp = temp.strip()
                temp = float(temp)
                data.append(temp)
            except Exception as ex:
                print(ex)
        print(data)
        pred = model.predict([data])[0]
        print(pred)
        pred = d[pred]
        print(pred)
        # result = pred[0]

    return render_template("home.html", result=pred)


if __name__ == '__main__':
    debug = True
    app.run()
