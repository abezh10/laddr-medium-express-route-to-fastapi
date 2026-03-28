"""Starter router module for Express Route to FastAPI."""


def get_report_preview():
    return {
        "ok": True,
        "message": "Starter router response",
        "range": "30d",
    }
