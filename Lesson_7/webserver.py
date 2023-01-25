from flask import Flask, render_template, request, redirect, send_file
import requests
from bs4 import BeautifulSoup
import os
import zipfile
import threading

app = Flask("TEST")

@app.route('/')
def index():
    return render_template("downloader.html")

@app.route('/manager')
def manager():
    url=""
    url=request.args.get('data')
    threads = []
    for threadNumber in range (0, 2):
        threads.append(threading.Thread(target=process(url,threadNumber), args=(threadNumber, )))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return redirect('/')

def process(url,threadNumber):
    headers = {
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.wikipedia.org/',
    'Connection': 'keep-alive',
    }
    r = requests.get(url=url, headers=headers)
    print(r)
    soup = BeautifulSoup(r.text, 'html.parser')
    filename = 0
    for img in soup.findAll('img'):
        filename = filename + 1
        image_temp = img.get('src')
        if image_temp[:1] == '/':
            image_path = url + image_temp
        else:
            image_path = image_temp
        file_name_temp = img.get('alt')
        if len(file_name_temp) == 0:
            file_name = str(index)
        else:
            file_name = file_name_temp
        if '.jpg' in image_path:
            image = os.getcwd()
            try:
                os.makedirs('Images/JPEG')
            except:
                folder_dir = image + '/Images/JPEG'
                name_file = "{}.jpg".format(file_name)
                final_path = os.path.join(folder_dir, name_file)
                with open(final_path , 'wb') as f:
                    f.write(requests.get(image_path).content)
                    print ("Thread #" + str(threadNumber)+ ": jpg")
        if '.png' in image_path:
            image = os.getcwd()
            try:
                os.makedirs('Images/PNG')
            except:
                folder_dir = image + '/Images/PNG'
                name_file = "{}.png".format(file_name)
                final_path = os.path.join(folder_dir, name_file)
                with open(final_path , 'wb') as f:
                    f.write(requests.get(image_path).content)
                    print ("Thread #" + str(threadNumber)+ ": png")
    

@app.route('/download_file')
def download_file():
    folder_to_be_zipped = 'Images'
    with zipfile.ZipFile('Images.zip', 'w', zipfile.ZIP_DEFLATED) as newzip:
        for dirpath, dirnames, files in os.walk(folder_to_be_zipped):
            for file in files:
                newzip.write(os.path.join(dirpath, file))
    path = "Images.zip"
    return send_file(path,as_attachment=True)



app.run(host="0.0.0.0", port=8081)