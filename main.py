from flask import Flask, Response
from itertools import chain
app, url = Flask(__name__), "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' width='1000' height='1000'><foreignObject width='1000' height='1000'><body xmlns='http://www.w3.org/1999/xhtml'>%s</body></foreignObject></svg>" % open("index.html").read().replace("\n", " ")
for rule in chain(app.url_rule_class("/|", endpoint='/|').get_rules(app.url_map), app.url_rule_class("/", endpoint='/').get_rules(app.url_map)):
    rule.bind(app.url_map)
    app.url_map._rules.append(rule)
    app.url_map._rules_by_endpoint.setdefault(rule.endpoint, []).append(rule)
app.view_functions = {'/' : lambda: Response(headers={"link":"<|>;rel=stylesheet;"}), '/|': lambda: "body{background-image:url(\"%s\");background-repeat:no-repeat;}" % url}
if __name__ == "__main__": app.run()