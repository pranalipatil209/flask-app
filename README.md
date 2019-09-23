# flask-app
Python flask app to read text files queried by user.

On call to this route application a read content of given file (see file1.txt.. file4.txt) and render properly it in HTML page.

After installing all dependencies, run the app by entering its folder and typing:

$ python app.py

Route call should be like,

http://localhost:5000/file3.txt

You can add query params with keys startline and endline

http://localhost:5000/file3.txt?startline=2&endline=56
