from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask("TEST")

@app.route('/posts')
def index():
    tableToPlace = "<div>"
    temp = open("Desk.txt", "r")
    for line in temp.readlines():
        tableToPlace += line
    tableToPlace += "</div>"
    temp.close()
    return render_template("posts.html", contents=tableToPlace)

@app.route('/editor')
def process():
    temp = open("Desk.txt", "a")
    button = request.args.get("operation")   
    match button : 
        case "Add" :
            temp.write("<div  class='title'>"+ '"'+str(request.args.get('title'))+ '"' + "</div>") 
            temp.write("<div  class='data'>"+ "-"+str(request.args.get('data')) + "</div>") 
            temp.write("<div class='time'>" + time()+ "</div>\n") 
    return render_template("editor.html")

@app.route('/admin')
def admin():
    button = request.args.get("Delete") 
    match button : 
        case "del" :
            inputFile = "Desk.txt"
            with open(inputFile, 'r') as filedata:
                inputFilelines = filedata.readlines()
                lineindex = 1
                deleteLine = int(request.args.get('variant'))
                with open(inputFile, 'w') as filedata:
                    for textline in inputFilelines:
                        if lineindex != deleteLine:
                            filedata.write(textline)
                            lineindex += 1
                        else:
                            lineindex += 1
            filedata.close()

    tableToPlace = "<table border=\"1\">"
    temp = open("Desk.txt", "r")
    counter = 1
    for line in temp.readlines():
        tableToPlace += "<tr><td>" + str(counter) + "</td><td>" + "Article number  " + str(counter) + "</td></tr>"
        counter += 1
    tableToPlace += "</table>"
    temp.close()

    return render_template("admin.html", contents=tableToPlace)

def time():
    time = datetime.now()
    time = time.strftime("%Y-%m-%d  %H:%M:%S")
    return time

app.run(host="0.0.0.0", port=8081)