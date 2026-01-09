from dataclasses import dataclass


@dataclass
class Actor(db.Model):
    id: int
    first_name: str
    last_name: str
