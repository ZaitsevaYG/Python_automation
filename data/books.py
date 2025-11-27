import dataclasses


@dataclasses.dataclass
class Book:
    title: str
    author: str
    price: str
    url: str