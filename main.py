import os
import sys
import traceback
from fastapi import FastAPI
import uvicorn

print("=== RAILWAY DEBUG START ===")
print(f"Python version: {sys.version}")
print(f"Current working directory: {os.getcwd()}")
print(f"PORT environment variable: {os.environ.get('PORT', 'NOT SET')}")
print(f"All environment variables:")
for key, value in os.environ.items():
    if 'API' in key or 'PORT' in key or 'HOST' in key:
        print(f"  {key}: {value}")
print("=== END DEBUG INFO ===")

app = FastAPI(title="Railway Test", version="1.0.0")

@app.get("/")
async def root():
    return {
        "message": "Railway test server is working!",
        "port": os.environ.get("PORT", "not-set"),
        "cwd": os.getcwd(),
        "python_version": sys.version
    }

@app.get("/health")
async def health():
    return {"status": "ok", "service": "railway-test"}

@app.get("/env")
async def env_check():
    return {
        "port": os.environ.get("PORT"),
        "api_key_set": bool(os.environ.get("API_KEY")),
        "base_url": os.environ.get("BASE_URL", "not-set"),
        "transport": os.environ.get("TRANSPORT", "not-set")
    }

if __name__ == "__main__":
    try:
        # Get port from Railway
        port = int(os.environ.get("PORT", 8080))
        host = "0.0.0.0"
        
        print(f"Starting server on {host}:{port}")
        
        # Railway-specific uvicorn config
        uvicorn.run(
            app, 
            host=host, 
            port=port,
            log_level="info",
            access_log=True
        )
    except Exception as e:
        print(f"ERROR starting server: {e}")
        print(f"Traceback: {traceback.format_exc()}")
        sys.exit(1)
