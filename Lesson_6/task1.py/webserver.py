from flask import Flask, render_template, request, redirect
import databaseWorker 


app = Flask("Lesson6")

@app.route('/chat')
def index():
    return render_template("chat.html",messages=databaseWorker.getMessage())

@app.route('/delete')
def delete():
    databaseWorker.databaseDel()
    return redirect("/chat")

@app.route('/send')
def sendmessage():
    login= request.args.get('login')
    message= request.args.get('message')
    time= databaseWorker.time()
    databaseWorker.addMessage(login,message,time)
    return redirect("/chat")

app.run(host="0.0.0.0", port=8081)

