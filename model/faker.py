def register(user_id, firstname, lastname):
    return get_user(user_id, firstname, lastname)


def get_user(user_id, firstname="", lastname=""):
    return {
        "user_id": user_id,
        "firstname": firstname,
        "lastname": lastname
    }
