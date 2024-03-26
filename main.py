#import package
from fastapi import FastAPI, Request, Response, HTTPException, Header

#create new object
app = FastAPI()

#API token key
API_KEY = "mimi"

#create endpoint -> home
@app.get('/')
def getHome():
    return{
        "message":"Welcome to my API"
    }

#API header
@app.get('/see-headers')
def readHeaders(request:Request):
    #mengambil header dari Request
    headers = request.headers

    print(headers.items)

    return{
        "message":"isi headers",
        "headers": headers.get('User-Agent')
    }

#Example 1 without authorization and custom header
@app.get("/example")
def read_example_headers(request: Request):
    headers = request.headers
    # Access specific header values
    user_agent = headers.get("user-agent")
    authorization = headers.get("authorization")
    custom_header = headers.get("custom-header")

    return {
        "User-Agent": user_agent,
        "Authorization": authorization,
        "Custom-Header": custom_header
    }

#Example 2 with authorization and custom header
@app.get("/example2")
def example_endpoint():
    content = "Hello, this is the response content."

    # Create a Response object and set custom headers
    response = Response(content=content)
    response.headers["X-Custom-Header"] = "This is custom value"
    response.headers["Authorization"] = "pass_token_1234"

    return response

@app.get("/")
def home():
  return {"message":"This is my API. Welcome!"}

#API authenticated - Create API key
@app.get("/protected")
def protect(api_key: str = Header(None)):

  if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

  return {
      "message":"Susu"
          }

@app.get("/protected2")
def protect(api_key: str = Header(None)):

  if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

  return {"message":"This endpoint is protected by API Token Key.",
          "data":{"1":{"username":"raka","password":"kembar1"},
                  "2":{"username":"riki","password":"kembar2"},
                  "3":{"username":"rokok","password":"kembar3"}
                 }
          }