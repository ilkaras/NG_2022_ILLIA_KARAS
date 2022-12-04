from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask("TEST")

@app.route('/')
def index():
    tableToPlace = "<table border=\"1\">"
    temp = open("users.txt", "r")
    result = 0
    for line in temp.readlines():
        result = line
    tableToPlace += "</td><td>" + str(result) + "</td></tr>"
    tableToPlace += "</table>"
    temp.close()
    return render_template("index.html", contents=tableToPlace)

@app.route('/process')
def process():
    temp = open("users.txt", "a")
    button = request.args.get("operation")   
    match button : 
        case "plus" :
            temp.write(request.args.get('data') + "+") 
        case "minus" :
            temp.write(request.args.get('data') + "-")
        case "multiply" :
            temp.write(request.args.get('data') + "*")
        case "devide" :
            temp.write(request.args.get('data') + "/")
        case "v stepen" :
            temp.write(request.args.get('data') + "**")   
        case "pod koren" :
            temp.write(request.args.get('data') + "** 0.5")   
        case "Clear" :
            temp = open('users.txt', 'r+')
            temp.truncate(0)
            temp.close()
        case "Result" :
            temp.write(request.args.get('data') + "\n")
            temp.close()
            return redirect('/calculate')
    return redirect('/')

@app.route('/calculate')
def calculate():
    temp = open('users.txt', 'r')
    tableToPlace = "<table border=\"1\">"
    calculated = 0
    for line in temp.readlines():
        calculated = line
    compiled_str = compile(calculated, 'string', 'eval')
    tableToPlace += "</td><td>" + "Result:" + str(eval(compiled_str)) + "</td></tr>"
    tableToPlace += "</table>"
    temp.close()
    return render_template("index.html", contents=tableToPlace)
    
app.run(host="0.0.0.0", port=8081)