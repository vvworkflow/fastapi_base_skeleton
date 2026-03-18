from fastapi import FastAPI
import uvicorn

app = FastAPI()


def main():
    pass


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8001)
