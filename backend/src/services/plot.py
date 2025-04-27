"""Service for generating plots with business logic."""

from io import BytesIO

import matplotlib.pyplot as plt

from services.total import get_total
from util.local import City


def get_plot_bytes(exemptions: int, quality: str, k: int):
    """Get the bytes for the plot of the three-way comparison between saving amounts."""
    y1, y2, y3, salaries = [], [], [], []
    counter = 80000
    for _ in range(20):
        salaries.append(counter)
        y1.append(
            get_total(counter, "california", exemptions, quality, k, City("other"))
        )
        y2.append(get_total(counter, "texas", exemptions, quality, k, City("other")))
        y3.append(get_total(counter, "new york", exemptions, quality, k, City("nyc")))
        counter += 20000

    plt.figure(figsize=(10, 6))
    plt.plot(salaries, y1, label="California", marker="o")
    plt.plot(salaries, y2, label="Texas", marker="s")
    plt.plot(salaries, y3, label="New York", marker="x")

    plt.title("Salary Against Savings")
    plt.xlabel("Salary")
    plt.ylabel("Savings")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()

    return buf
