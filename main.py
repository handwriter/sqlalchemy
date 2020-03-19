from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.sqlite")
    captain = User()
    captain.surname = 'Scott'
    captain.name = 'Ridley'
    captain.age = 21
    captain.position = 'captain'
    captain.speciality = 'research engineer'
    captain.address = 'module_1'
    captain.email = 'scott_chief@mars.org'
    user1 = User()
    user1.surname = 'Max'
    user1.name = 'Riddel'
    user1.age = 47
    user1.position = 'ex-captain'
    user1.speciality = 'physic engineer'
    user1.address = 'module_7'
    user1.email = 'mx.riddel@mars.org'
    user2 = User()
    user2.surname = 'Scaut'
    user2.name = 'Cherly'
    user2.age = 31
    user2.position = 'high enginer'
    user2.speciality = 'theory engineer'
    user2.address = 'module_4'
    user2.email = 'cheerly@mars.org'
    user3 = User()
    user3.surname = 'Presnyakov'
    user3.name = 'Nikita'
    user3.age = 28
    user3.position = 'mechanic'
    user3.speciality = 'mechanic'
    user3.address = 'module_2'
    user3.email = 'press_n@mars.org'
    session = db_session.create_session()
    session.add(captain)
    session.add(user1)
    session.add(user2)
    session.add(user3)
    session.commit()
    app.run()


if __name__ == '__main__':
    main()