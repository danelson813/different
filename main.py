from domain.helpers import People, Person


joe =  Person('Joe', 25, 1.85, 'joe@dataquest.io', (40.748441, -73.985664))
mary = Person('Mary', 43, 1.67, 'mary@dataquest.io', (-73.985664, 40.748441))

print(joe < mary)