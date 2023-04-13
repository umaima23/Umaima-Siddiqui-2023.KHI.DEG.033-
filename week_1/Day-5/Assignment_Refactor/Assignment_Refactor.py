from typing import List
class User:
    sub: bool
def notify(user: User) -> None:
    pass
def get_subscribed_users(users: List[User]) -> List[User]:
    """Filter Subscribed Users.."""
    return [user for user in users if user.subscribed]
def notify_subscribed_users(users: List[User]) -> None:
    """Notify to a given List of Subscribed Users."""
    for user in get_subscribed_users(users):
        notify(user)

