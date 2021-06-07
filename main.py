from flask import Flask, Response
app, url = Flask(__name__), "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' width='1000' height='1000'><foreignObject width='1000' height='1000'><body xmlns='http://www.w3.org/1999/xhtml'>%s</body></foreignObject></svg>" % open("index.html").read().replace("\n", " ")
@app.route('/|')
def style():
    return "body{background-image:url(\"%s\");background-repeat:no-repeat;}" % url
@app.route('/')
def index():
    return Response(headers={"link":"<|>;rel=stylesheet;"})
app.run(debug=True)