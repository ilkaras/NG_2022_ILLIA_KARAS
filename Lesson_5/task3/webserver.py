from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask("TEST")

@app.route('/posts')
def index():
    tableToPlace = "<div>"
    temp = open("Lorem_Ipsum.txt", "r")
    for line in temp.readlines():
        tableToPlace += line
    tableToPlace += "</div>"
    temp.close()
    return render_template("posts.html", contents=tableToPlace)

@app.route('/editor')
def process():
    temp = open("Lorem_Ipsum.txt", "a")
    button = request.args.get("operation")   
    match button : 
        case "Add" :
            temp.write("<div  class='title'>"+ str(request.args.get('title')) + "</div>") 
            temp.write("<div  class='data'>" + str(request.args.get('data')) + "</div>\n") 
            temp.write("<div class='time'>" + time()+ "</div>\n") 
    return render_template("editor.html")


def time():
    time = datetime.now()
    time = time.strftime("%Y-%m-%d  %H:%M:%S")
    return time

app.run(host="0.0.0.0", port=8081)