import random, string
from hashlib import pbkdf2_hmac
# Is a generic constructor that takes the string name of the desired algorithm
# as its first parameter. It also exists to allow access to the above listed
# hashes as well as any other algorithms that your OpenSSL library may offer.


def getHashPassword(password1, salts):
    return pbkdf2_hmac("sha256", password1.encode(), salts.encode(), 100)

def getSalt():
    character_choice = string.digits+string.punctuation+string.ascii_letters
    salts = "".join(random.choices(character_choice, k=10))
    return salts



# hashing is one way
# more secure for purpose of passwords as you don't want to get password back, you wanna check you have the same one
# adding salts: - make hash appear more random     - password hash will be different for users that have same password as you are generating a different salt each time
# attackers would have to create a rainbow table to crack salts
