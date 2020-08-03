# Create an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True:
user1 = {
    'name': 'Annie',
    'valid': 0  # changing this will either run or not run the message_friends function.
}


def authenticated(fn):
    def check(*args, **kwargs):
        if args[0]['valid'] == True:
            res = fn(*args, **kwargs)
            return res

    return check


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
