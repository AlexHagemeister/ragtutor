from fastapi import FastAPI

from .models import UserQuery

# Your docs are available at /docs
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/query")
def query(user_query: UserQuery) -> str:
    """Main endpoint to query the bot"""
    # Send data to Query Filter Agent
    # TODO: Implement Query Filter Agent
    # Send Filtered Query to Pincone DB
    # TODO: Implement Pincone DB
    # Send Pinecond data to Query Response Agent
    # TODO: Implement Query Response Agent
    # NOTE: Return just the response text to the end user!
    # return response_text

    # NOTE: This is a placeholder response
    return "Here's your damn response!"
