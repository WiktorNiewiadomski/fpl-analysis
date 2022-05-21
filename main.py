from typing import Union
from fastapi import FastAPI
from fantasy_football_hub import FantasyFootballHub

app = FastAPI()

fpl_hub = FantasyFootballHub()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/players-stats/{token}")
def players_stats(token: str):
    return fpl_hub.players_stats(token)
