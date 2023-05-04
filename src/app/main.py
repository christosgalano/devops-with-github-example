import uvicorn
from fastapi import FastAPI, status

app = FastAPI(
    docs_url="/",
    redoc_url="/redocs",
)


@app.get("/{string}", response_model=str, status_code=status.HTTP_200_OK)
def get_hello_1(string: str):
    return f"Hello {string}"


@app.get("/{string_1}/{string_2}", response_model=str, status_code=status.HTTP_200_OK)
def get_hello_2(string_1: str, string_2: str):
    return f"Hello {string_1}, {string_2}"


@app.get(
    "/{string_1}/{string_2}/{string_3}",
    response_model=str,
    status_code=status.HTTP_200_OK,
)
def get_hello_3(string_1: str, string_2: str, string_3: str):
    return f"Hello {string_1}, {string_2}, {string_3}"

@app.get(
    "/{string_1}/{string_2}/{string_3}/{string_4}",
    response_model=str,
    status_code=status.HTTP_200_OK,
)
def get_hello_4(string_1: str, string_2: str, string_3: str, string_4: str):
    return f"Hello {string_1}, {string_2}, {string_3}, {string_4}"

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
