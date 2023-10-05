import bcrypt

def GetHashPassword(password):
    bytes = password.encode('utf-8')
    hash = bcrypt.hashpw(bytes, bcrypt.gensalt())
    hash_pass = hash.decode('utf-8')
    return hash_pass