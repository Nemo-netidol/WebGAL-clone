from fastapi import FastAPI, Request
import uvicorn
from AI.deepseek import generate_response, generate_response_from_file

app = FastAPI()

@app.post("/input")

async def receive_input(request: Request):
    data = await request.json()
    user_input = data.get("input", "")
    with open("input.txt", "w") as file:
        file.write(user_input)

    generate_response_from_file("input.txt")
    # Or you can use this function to generate response by passing user input directly to the AI

    #generate_response(user_input)

    return {"status": "success", "received": user_input}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001)