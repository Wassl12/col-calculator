"""Entrypoint for fastapi server."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

from config.config import Config
from services.plot import get_plot_bytes
from services.total import get_total
from util.local import City

app = FastAPI()

origins = Config.ALLOWED_ORIGINS.split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["OPTIONS"],
    allow_headers=["*"],
)


@app.get("/savings/{state}/{salary}/{exemptions}/{quality}/{k}")
def get_savings(
    salary: int, state: str, exemptions: int, quality: str, k: int, city: str = "other"
):
    "Get savings for a typical city in a particular state."
    total = get_total(salary, state, exemptions, quality, k, City(city))

    return {"amount": total}


@app.get("/savings/{exemptions}/{quality}/{k}")
def plot_big_three(exemptions: int, quality: str, k: int):
    """Plot three large living scenarios."""
    buf = get_plot_bytes(exemptions, quality, k)
    return StreamingResponse(buf, media_type="image/png")
