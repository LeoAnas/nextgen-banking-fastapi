from fastapi import FastAPI


app=FastAPI(
    title="NextGen Bank",
    description="Fully featured fastapi banking api "
) 

@app.get("/")
def home():
    return{"Hello":"Banking API"}