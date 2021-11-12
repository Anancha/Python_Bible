from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import Form 
app = FastAPI()

@app.post("/login")
def login(username:str=Form(...),password:str=Form(...)):
    if (username == "orapin") and (password == "python"):
        return JSONResponse(status_code=200,content={"Message":"Login Success."})
    else:
        return JSONResponse(status_code=403,content={"Message":"Login Fail."})