from pathlib import Path
import fastapi as fa
from pydantic import BaseModel
from yeelight import Bulb, discover_bulbs
from typing import Tuple


app = fa.FastAPI()

_fe_dir = Path(__file__).parent.parent / "fe"

class Status(BaseModel):
    bulb_name: str
    power_status: str
    brightness: int
    colour: Tuple[int, int, int]
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
    print(f"static path: {path}")
    return fa.responses.FileResponse(
        path=_fe_dir / path,
    )

@app.get("/turn_on")
def hello():
    bulb.turn_on()
    return "Hello from the server!"

@app.get("/api/v1/status")
def status():
    #Use the `bulb` variable to get the properties of the LED strip, such as its name, power status, brightness, and color. Return these properties as an instance of the `Status` class.
    # bulb_name = bulb.get_properties()['name']
    # power_status = bulb.get_properties()['power']
    # brightness = bulb.get_properties()['bright']
    # colour = bulb.get_properties()['rgb']
    # print(f"Bulb name: {bulb_name}, Power status: {power_status}, Brightness: {brightness}, Colour: {colour}")
    return Status(
        bulb_name='test',
        power_status='on',
        brightness=0,
        colour=(0xFF, 0xFF, 0xFF)
    )

@app.post("/api/v1/turn_on")
def turn_on():
    bulb.turn_on() 
    return "Turned on light"

@app.post("/api/v1/turn_off")
def turn_off():
    bulb.turn_off()
    return "Turned off light"

bulb = None

def discover_bulb():
    bulbs = discover_bulbs()
    bulb_ip = bulbs[0]['ip']
    bulb = Bulb(bulb_ip)
    return bulb

bulb = discover_bulb()
print(bulb)

bulb.turn_off()
test = status()
# todo other things like turn_off, set_colour, etc.
