from pathlib import Path
import fastapi as fa
from pydantic import BaseModel
from yeelight import Bulb, discover_bulbs


app = fa.FastAPI()

_fe_dir = Path(__file__).parent.parent / "fe"

class Status(BaseModel):
    bulb_name: str
    power_status: str
    brightness: int
    colour: int
    # ... other useful things regarding service status?
    # colour? brightness? etc..


# statically serve the frontend
@app.get("/")
def index():
    # redirect to the frontend's index.html
    return fa.responses.RedirectResponse(
        url="/static/index.html",
    )

# serve the frontend's static assets
@app.get("/static/{path:path}")
def static(path: str):
    return fa.responses.FileResponse(
        path=_fe_dir / path,
    )


@app.get("/api/v1/status")
def status():
    return Status(
        bulb_name="TODO",
    )

@app.post("/api/v1/turn_on")
def turn_on():
    
    # TODO turn bulb on here
    return "Hello from the server! implement this function"

bulb = None

def discover_bulb():
    global bulb
    bulbs = discover_bulbs()
    bulb_ip = bulbs[0]['ip']
    bulb = bulb_ip

discover_bulb()


# todo other things like turn_off, set_colour, etc.
