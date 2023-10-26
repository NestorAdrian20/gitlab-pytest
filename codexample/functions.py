
def return_value(value):
    return value

def raise_error(msg_kw):
    raise ValueError(f"Exception {msg_kw} raised")

def factorielle(n):
    if n == 0:
        return 1
    else:
        return n  * factorielle(n-1)
