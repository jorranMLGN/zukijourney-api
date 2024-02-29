from fastapi import APIRouter, Response
import json

app = APIRouter()

with open('data/models/rp/list.json', 'r') as f:
    data = json.load(f)

@app.route("/unf/models", methods=["GET", "POST", "PUT", "PATCH", "HEAD"])
async def models(_) -> None:
    return Response(json.dumps(data, indent=4), media_type="application/json")