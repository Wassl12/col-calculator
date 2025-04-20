from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO

from util.local import City
from services.total import get_total

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/savings/{state}/{salary}/{exemptions}/{quality}/{k}')
def root(salary: int, state: str, exemptions: int, quality: str, k: int, city: str = "other"):
    total = get_total(salary, state, exemptions, quality, k, City(city))

    return {"amount": total}

@app.get('/savings/{exemptions}/{quality}/{k}')
def plot(exemptions: int, quality: str, k: int):

    y1 = []
    y2 = []
    y3 = []
    salaries = []
    counter = 80000
    for i in range(20):
        salaries.append(counter)
        y1.append(get_total(counter, "california", exemptions, quality, k, City("other")))
        y2.append(get_total(counter, "texas", exemptions, quality, k, City("other")))
        y3.append(get_total(counter, "new york", exemptions, quality, k, City("nyc")))
        counter += 20000

    plt.figure(figsize=(10, 6))
    plt.plot(salaries, y1, label='California', marker='o')
    plt.plot(salaries, y2, label='Texas', marker='s')
    plt.plot(salaries, y3, label='New York', marker='x')

    # Add titles and labels
    plt.title('Line Chart with Custom Data')
    plt.xlabel('Salary')
    plt.ylabel('Savings')
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    # Return image as a StreamingResponse
    return StreamingResponse(buf, media_type="image/png")



