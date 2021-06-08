from dflask import DirectFlask, Response
from itertools import chain
app, url = DirectFlask(__name__), "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' width='1000' height='1000'><foreignObject width='1000' height='1000'><body xmlns='http://www.w3.org/1999/xhtml'>%s</body></foreignObject></svg>" % open("index.html").read().replace("\n", " ")
app.add_response("/", Response(headers={"link":"<|>;rel=stylesheet;"}))
app.add_response("/|", "body{background-image:url(\"%s\");background-repeat:no-repeat;}" % url)
if __name__ == "__main__": app.run()