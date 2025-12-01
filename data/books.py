import dataclasses
from typing import Optional


@dataclasses.dataclass
class Book:
    title: str
    author: str
    price: str
    url: str
    id: Optional[str] = None
    slug: Optional[str] = None

    def __post_init__(self):
        if not self.url and self.id and self.slug:
            self.url = f"https://www.litres.ru/book/{self.slug}-{self.id}/"


ATOMIC_HABITS = Book(
    title="Атомные привычки. Как приобрести хорошие привычки и избавиться от плохих",
    author="Джеймс Клир",
    price='',
    url='',
    id="48514275",
    slug="dzheyms-klir/atomnye-privychki-kak-priobresti-horoshie-privychki-i-izbavit"
)

