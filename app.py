import flask
import requests

app = flask.Flask(__name__)

@app.get("/")
def landing():
    print("Header host is ", flask.request.host)
    source_ip = flask.request.environ.get('HTTP_X_FORWARDED_FOR', flask.request.remote_addr)
    return "Connection successful {0}\n".format(source_ip)

@app.get("/source_ip")
def source_ip():
    result = {
        "Source IP":flask.request.remote_addr,
        "Header-Host":flask.request.host, 
        "This application's exposed IP":"N/A"}
    print("Checking on the log")
    return flask.jsonify(result), 200

@app.get("/all_request")
def all_request():
    print(flask.request.headers.items)
    return "ohd"

@app.get("/test")
def test():
    print("something")
    return "Connection successful"

@app.get("/send_request_ip")
def send_request_ip():
    args = flask.request.args
    target_addr = args.get("ip")
    target_addr_split = target_addr.split(":")
    ip = target_addr_split[0]
    port = target_addr_split[1]
    print("sending request to", ip, port)
    return requests.get(ip)

#curl 127.0.0.1:5000/send_request_url?url="https://dongsootestfree.azurewebsites.net/source_ip"
@app.get("/send_request_url")
def send_request_url():
    args = flask.request.args
    target_url = args["url"]
    print("sending request to", target_url)
    res = requests.get(target_url)
    return res.content