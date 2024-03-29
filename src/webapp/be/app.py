import os
from pathlib import Path
import fastapi as fa
from pydantic import BaseModel
from yeelight import Bulb
from typing import Tuple


app = fa.FastAPI()

_fe_dir = Path(__file__).parent.parent / "fe"

BULB_IP = os.environ.get("BULB_IP")


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
    # Use the `bulb` variable to get the properties of the LED strip
    # Such as its name, power status, brightness, and color.
    # Return these properties as an instance of the `Status` class.
    properties = bulb.get_properties()
    bulb_name = properties["name"] or "Unknown"
    power_status = properties["power"]
    brightness = int(properties["bright"])
    colour = _int_to_colour(int(properties["rgb"]))
    return Status(
        bulb_name=bulb_name,
        power_status=power_status,
        brightness=brightness,
        colour=colour,
    )


@app.post("/api/v1/turn_on")
def turn_on():
    return bulb.turn_on()


@app.post("/api/v1/turn_off")
def turn_off():
    return bulb.turn_off()


def _int_to_colour(colour: int) -> Tuple[int, int, int]:
    return (
        (colour >> 16) & 0xFF,
        (colour >> 8) & 0xFF,
        colour & 0xFF,
    )


@app.post("/api/v1/set_brightness/")
def set_brightness(brightness: int):
    # convert brightness to integer if it's a string
    if isinstance(brightness, str):
        brightness = brightness
    # set the brightness of the bulb
    bulb.set_brightness(brightness)
    # return confirmation string
    return f"Brightness set to {brightness}%"


@app.post("/api/v1/set_colour/")
def set_colour(red: int, green: int, blue: int):
    if red == 0 and green == 0 and blue == 0:
        raise fa.HTTPException(
            status_code=400,
            detail="Invalid RGB values: (0, 0, 0) not allowed. Use the turn off method instead.",
        )
    bulb.set_rgb(red, green, blue)
    return f"Colour set to R: {red}, G: {green}, B: {blue}"


bulb = Bulb(BULB_IP)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
