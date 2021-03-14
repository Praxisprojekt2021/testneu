from neomodel import (config, StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo)
import configparser


class Country(StructuredNode):
    code = StringProperty(unique_index=True, required=True)


class Person(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    age = IntegerProperty(index=True, default=0)

    # traverse outgoing IS_FROM relations, inflate to Country objects
    country = RelationshipTo(Country, 'IS_FROM')


def init_db():
    parser = configparser.ConfigParser()
    # REPLACE PATH
    parser.read_file(open(r'C:\Users\aaron\PycharmProjects\testneu\neo4j\config.txt'))
    config.DATABASE_URL = 'bolt://{}:{}@{}:{}'.format(parser.get('neo4j', 'user'), parser.get('neo4j', 'password'),
                                                      parser.get('neo4j', 'ip'), parser.get('neo4j', 'port')).replace(
        '"',
        '')


def add_person():
    name = 'Aaron'
    age = 321
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
    init_db()
    a = 1
    while (a):
        try:
            contents = Person.nodes.get(name='Aaron')
        except:
            add_person()
        else:
            a = 0

    print(config.DATABASE_URL)
    # IDE says can be undefined, while loop in main does not allow for that though
    print(contents)
