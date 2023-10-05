from repository import collection

def RegisterRepo(user):
    print("---------Masuk ke repo user---------------")
    success = collection.insert_one({"_id" : user._id, "username" : user.username, "email" : user.email, "password" : user.password})
    if success:
        return True
    else:
        return False    