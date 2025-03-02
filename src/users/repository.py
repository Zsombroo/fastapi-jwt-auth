from src.users.model import User


def get_user(
    username: str,
) -> User | None:
    """ TODO: Implement a proper database connection and query to fetch user data
    """
    if username != "testuser":
        return None
    
    return User(
        username="testuser",
        hashed_pw="$2b$12$DIcc2YlzRg5A4gbXaeHKXuXwR95qHuw8QLMSedf7ZCqz5wOBFE5cq",
        teams=["Team_A", "Team_B"],
    )
