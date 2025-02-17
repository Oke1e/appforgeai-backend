from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS settings (allows frontend to connect)
origins = [
    "http://localhost:3000",  # Local frontend (for development)
    "https://appforgeai-frontend.vercel.app"  # Deployed frontend on Vercel
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# ✅ Root route (for basic status check)
@app.get("/")
def read_root():
    return {"message": "Backend is running!"}

# ✅ API Route for Chatbot Communication
@app.post("/api/chat")
async def chat_endpoint(request: Request):
    data = await request.json()
    return {"reply": f"Received: {data['message']}"}
