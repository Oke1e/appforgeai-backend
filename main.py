from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging

app = FastAPI()

# ✅ Allow frontend to communicate with backend
origins = [
    "http://localhost:3000",
    "https://appforgeai-frontend.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # ✅ Allow all HTTP methods
    allow_headers=["*"],  # ✅ Allow all headers
)

# ✅ Enable logging for debugging
logging.basicConfig(level=logging.INFO)

@app.get("/")
def read_root():
    return {"message": "Backend is running!"}

# ✅ Define the expected request body
class ChatRequest(BaseModel):
    message: str
    category: str = "other"

@app.post("/api/chat")  # ✅ Ensure this route properly handles POST requests
async def chat_endpoint(request: ChatRequest):
    message = request.message
    category = request.category

    logging.info(f"Received message: {message} | Category: {category}")

    # ✅ Process category logic (this will later be expanded)
    response_message = f"Received: {message} - Category: {category}"
    
    return {"reply": response_message}
