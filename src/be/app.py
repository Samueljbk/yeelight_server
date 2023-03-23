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
    return fa.responses.FileResponse(
        path=_fe_dir / path,
    )

@app.get("/api/v1/status")
def status():
    #Use the `bulb` variable to get the properties of the LED strip, such as its name, power status, brightness, and color. Return these properties as an instance of the `Status` class.
    properties = bulb.get_properties()
    bulb_name_variable = properties['name'] or "Unknown"
    power_status = properties['power']
    brightness = properties['bright']
    colour = properties['rgb']
    if bulb_name_variable is None:
        bulb_name_variable = 'Unknown'
    print(f"Bulb name: {bulb_name_variable}, Power status: {power_status}, Brightness: {brightness}, Colour: {colour}")
    return Status(
        bulb_name= bulb_name_variable,
        power_status='on',
        brightness=0,
        colour=(0xFF, 0xFF, 0xFF)
    )

@app.post("/api/v1/turn_on")
def turn_on():
    bulb.turn_on() 
    return bulb.turn_on()

@app.post("/api/v1/turn_off")
def turn_off():
    bulb.turn_off()
    return bulb.turn_off()

def discover_bulb():
    bulbs = discover_bulbs()
    for bulb in bulbs:
        if bulb['capabilities']['name'] == 'Sam':
            bulb_ip = bulb['ip']
            bulb = Bulb(bulb_ip)
            return bulb

def _int_to_colour(colour: int) -> Tuple[int, int, int]:
    return (
        (colour >> 16) & 0xFF,
        (colour >> 8) & 0xFF,
        colour & 0xFF,
    )

bulb = None
bulb = discover_bulb()
print(bulb)
# todo other things like turn_off, set_colour, etc.


