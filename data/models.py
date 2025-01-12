from dataclasses import dataclass


@dataclass
class Analysis:
    short_name: str
    full_name: str
    count: int

eli = Analysis(short_name="ЭЛИ", full_name="ЭЛИ-Н-ТЕСТ", count=5)
