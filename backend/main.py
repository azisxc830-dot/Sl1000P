
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Sl1000P API",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://azisxc830-dot.github.io"
    ],
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "app": "Sl1000P",
        "status": "ready",
        "mode": "offline"
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "mt5_connected": False,
        "mode": "offline"
    }


@app.get("/mt5/status")
def mt5_status():
    return {
        "connected": False,
        "broker": None,
        "message": (
            "MT5 bridge belum dikonfigurasi"
        )
    }
