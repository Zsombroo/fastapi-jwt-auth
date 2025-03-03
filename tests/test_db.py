from sqlalchemy.orm import Session
from src.db import engine
from src.db import init_db
from src.db import destroy_db
from src.db.schemas import Team
from src.db.schemas import User
from src.db.schemas import UserTeamJunction
    

def create_example_data(session):
    user1 = User(
        username="test_user",
        email="test_email@example.com",
        hashed_password="hashed_password_here"
    )
    user2 = User(
        username="test_user222",
        email="test_email@example.com",
        hashed_password="hashed_password_here"
    )
    team = Team(team_name="test_team")
    session.add(user1)
    session.add(user2)
    session.add(team)
    session.commit()

    user_team_connection1 = UserTeamJunction(user_id=user1.id, team_id=team.id, role="Admin")
    user_team_connection2 = UserTeamJunction(user_id=user2.id, team_id=team.id, role="Admin")
    session.add(user_team_connection1)
    session.add(user_team_connection2)
    session.commit()


def query_data(session):
    from sqlalchemy import select

    stmt = select(User).filter(User.username=="test_user")
    print(
        session.execute(stmt).all()
    )
    # for i in session.query(User).all():
    #     print(i)

    # for i in session.query(Team).all():
    #     print(i)

    # for i in session.query(UserTeamJunction).all():
    #     print(i)


# def test_db():
#     init_db()
#     with Session(engine) as session:
#         create_example_data(session)
#         query_data(session)
#     destroy_db()
#     assert False

