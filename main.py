from fastapi import FastAPI
import os
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Railway deployment is working!", "status": "ok"}

@app.get("/health")
async def health():
    return {"status": "healthy", "port": os.environ.get("PORT", "8080")}

@app.get("/sse")
async def sse_test():
    return {"message": "SSE endpoint reachable", "note": "This would be the MCP SSE endpoint"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    print(f"Starting simple test server on port {port}")
    uvicorn.run(app, host="0.0.0.0", port=port)
