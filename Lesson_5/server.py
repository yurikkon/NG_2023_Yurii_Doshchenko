from flask import Flask,render_template,request,redirect


app = Flask("kek")
app.debug = True

register_list = {}
messages = []

@app.route('/')
def index():
    return render_template("Registration.html")

@app.route('/show_input', methods=['POST'])
def show_input():
    input1 = request.form['input1']
    input2 = request.form['input2']
    register_list[input1] = input2
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    UserName = request.form["input1"]
    PassWord = request.form["input2"]
    for key in register_list.keys():
        if key == UserName and register_list[key] == PassWord:
            return render_template("chat.html")
        else:
            label_text = 'wrong login or password'
            return render_template("login.html",label_text=label_text) 
        


@app.route("/chat", methods=['POST'])
def chatIng():
    message = request.form.get('message')
    if message:
        messages.append((message))
    return render_template('chat.html', messages=messages) 


app.run(host="0.0.0.0", port=8081)
