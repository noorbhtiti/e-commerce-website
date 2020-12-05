import hashlib


# HASHING METHOD

def hashfunc(password):
    temp = hashlib.sha256(password.encode('utf-8'))
    return temp.hexdigest()


# end of HASHING METHOD

# start of uppercase function#
def uppercase(email):
    return email.upper()

# end of uppercase function
