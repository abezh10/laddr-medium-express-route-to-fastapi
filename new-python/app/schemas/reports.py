"""Starter schema module for Express Route to FastAPI."""

from dataclasses import dataclass


@dataclass
class ReportRequest:
    range: str = "30d"
    include_archived: bool = False
