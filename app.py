#!/usr/bin/python
from flask import Flask, render_template, request
app = Flask(__name__)

import process
do_work = process.FILE_HANDELING()
@app.route('/',defaults={'filename': 'file1.txt'})
@app.route('/<filename>', methods=['GET'])
def readFile(filename):
    start = request.args.get('startline', default=0, type=int)
    end = request.args.get('endline', default=0, type=int)
    data = do_work._valid_file(filename)
    if data is True:
        temp = do_work._read_file(filename,start,end)
        if(temp == True):
            return render_template('output.html')
        else:
            return render_template('404.html', error=temp)
    else:
        return render_template('404.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)