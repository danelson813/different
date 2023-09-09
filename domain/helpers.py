from dataclasses import dataclass, field
from typing import Tuple
from typing import List


@dataclass(order=True)
class Person():
    sort_index: int = field(init=False, repr=False)
    name: str
    age: int
    height: float
    email: str
    house_coordinates: Tuple

    # def __repr__(self):
    #     return (f"This is a {self.__class__.__name__} called {self.name}")
    def __post_init__(self):
        self.sort_index = self.age


@dataclass
class People():
    people: List[Person]



# joe =  Person('Joe', 25, 1.85, 'joe@dataquest.io', (40.748441, -73.985664))
# mary = Person('Mary', 43, 1.67, 'mary@dataquest.io', (-73.985664, 40.748441))

# print(People([joe, mary]))
# print(joe)