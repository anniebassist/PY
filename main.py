from fastapi import FastAPI
app=FastAPI()

@app.get("/hello")
def sayHello():
 return "Hello Anirban1 and Ambika"