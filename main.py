from flask import Flask, render_template, request

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        temperature = float(request.form['temperature'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']

        if from_unit == 'celsius' and to_unit == 'fahrenheit':
            result = celsius_to_fahrenheit(temperature)
        elif from_unit == 'fahrenheit' and to_unit == 'celsius':
            result = fahrenheit_to_celsius(temperature)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

