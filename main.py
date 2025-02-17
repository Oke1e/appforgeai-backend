from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
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

@app.post("/api/chat")
async def chat_endpoint(request: Request):
    data = await request.json()
    message = data.get("message", "")
    category = data.get("category", "other")  # Default to "other" if no category is provided

    logging.info(f"Received message: {message} | Category: {category}")

    # ✅ Process category logic (this will later be expanded)
    response_message = f"Received: {message} - Category: {category}"
    
    return {"reply": response_message}
