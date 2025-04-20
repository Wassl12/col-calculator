from fastapi import FastAPI
from services.taxes import get_all_taxes
from util.state import Quality, State, get_rent, state_specific_expenses


app = FastAPI()

@app.get('/savings/{state}/{salary}/{exemptions}/{quality}/{k}')
def root(salary: int, state: str, exemptions: int, quality: str, k: int):
    after_401k = salary - k
    after_taxes = salary - get_all_taxes(salary, state, exemptions)

    total = after_taxes - get_rent(Quality(quality), State(state)) + k

    total -= state_specific_expenses(Quality(quality), State(state))

    return {"amount": total}



