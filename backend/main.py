from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from analyzer import analyze_logs

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health():
    return {"message": "AI Log Analyzer Running"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    
    content = await file.read()
    logs = content.decode("utf-8")

    result = analyze_logs(logs)

    return {
        "analysis": result
    }