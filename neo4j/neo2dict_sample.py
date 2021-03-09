"""
This shows how neo4j data can be delivered to the server as dict


TO RUN
install:
    pip install neomodel
run local:
    neo4j local database:
        user: neo4j
        password: 123456
        address: localhost:7687
"""

from neomodel import (config, StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo)

config.DATABASE_URL = 'bolt://neo4j:123456@localhost:7687'

name = 'Aaron'
age = 123

"""Not used yet"""


class Country(StructuredNode):
    code = StringProperty(unique_index=True, required=True)


class Person(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    age = IntegerProperty(index=True, default=0)

    # traverse outgoing IS_FROM relations, inflate to Country objects
    country = RelationshipTo(Country, 'IS_FROM')


def add_person():
    person = Person(name=name, age=age).save()
    person.save()
    print("Created Person with name ", person.name)


def output(get_contents):
    this_dict = {
        "id": contents.id,
        "uid": contents.uid,
        "name": contents.name,
        "age": contents.age,
    }

    print(type(this_dict), this_dict)


if __name__ == '__main__':
    a = 1
    while (a):
        try:
            contents = Person.nodes.get(name='Aaron')
        except:
            add_person()
        else:
            a = 0

    output(contents)
