from databaseWorker import *
from flask import Flask, render_template, redirect, request
import platform, psutil

app = Flask("TEST")

prepareDb("options.db")

specification = {
    "Computer network name": platform.node(),
    "Machine type": (str(platform.machine()) + "  "+ str(platform.processor())),
    "Processor": (str(platform.processor()) + "  " + "Phisical cores: " + str(psutil.cpu_count(logical=True))
     + "  " + "Logical processors:  " + str(psutil.cpu_count(logical=False))),
    "Platform type": platform.platform(),
    "Memory": (str(psutil.virtual_memory()) + str(psutil.swap_memory( ))),
    "Operating system release": platform.version(),
    "Disk": str(psutil.disk_io_counters(perdisk=False, nowrap=True)),
    }      
specification_name=[]
for key in specification.keys():
    specification_name.append(key.lower().replace(" ","_"))

@app.route('/')
def index():
    return render_template("menu.html", checkboxes=generateCheckboxes(specification_name),contents=getText("options.db"))

@app.route('/getdata')
def getdata():
    connection = init_conn("options.db")
    cursor = connection.cursor()
    cleardb()
    for name in specification_name:
        data = request.args.get(name)
        if data == "on":
            name = name.replace("_"," ").capitalize()
            sql = "INSERT INTO options(`name`,`text`) VALUES('{}','{}')".format(name,specification[name])
            cursor.execute(sql)
            connection.commit()
    connection.close()
    return redirect('/')

def generateCheckboxes(names):
    html = ""
    for element in names:
        html += f'''<div>
      <input type="checkbox" id="{element}" name="{element}" checked>
      <label for="{element}">{element}</label>
    </div>'''
    return html

app.run(host="0.0.0.0", port=8081)