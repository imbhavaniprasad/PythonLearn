from typing import Optional


def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")
# Using Optional[str] instead of just str will let the editor 
# help you detect errors where you could be assuming that a 
# value is always a str, when it could actually be None too.

# Optional[Something] is actually a shortcut for Union[Something, None], they are equivalent.
# This also means that in Python 3.10, you can use Something | None:None
# ex: def say_hi(name: str | None = None):

"""
Like /users/me, let's say that it's to get data about the current user.

And then you can also have a path /users/{user_id} to get data about a specific user by some user ID.

Because path operations are evaluated in order, you need to make sure that the path for /users/me is declared before the one for /users/{user_id}:
# you can also sue update to do the same

# item_dict = item.dict()
# response = {"item_id": item_id}
# response.update(item_dict)
"""

# Annotated can be used to add metadata to your parameters

# You can define background tasks to be run after returning a response by importing BackgroundTasks