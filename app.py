from flask import Flask, request
app = Flask(__name__)

stored_age = 26

@app.route('/')
def hello_oworld():
    return "Hello world!"

@app.route('/sheela')
def sheela():
    return f"Sheela ki jawan {stored_age}! "

@app.route('/sheela/<age>')
def sheela_age(age):
    return f"Sheela ki age {age}."

@app.route('/sheela',methods=['POST'])
def sheela_post():
    return "DONE"
    global stored_age
    age= request.form.get('age')
    stored_age=age


app.run()
