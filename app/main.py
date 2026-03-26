from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

my_name= "Sagar"

#main route for this API
@app.get("/")
def read_root():
    #f-string concatenation
    return { "msg": f"Hello {my_name}" }

#what is my IP
@app.get("/api/ip")
def api_ip(request: Request):

    return { "ip": request.client.host}


@app.get("/ip", response_class=HTMLResponse)
def html_ip(request: Request):

    return f"<h1>Your IP is {request.client.host}</h1>"

 