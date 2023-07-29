from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('indexs.html')
@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['expression']
    expression = expression.replace('×', '*').replace('÷', '/')
    result = eval(expression)
    return render_template('indexs.html', result=result)
if __name__ == '__main__':
    app.run()