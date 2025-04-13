from dataclasses import dataclass


# @dataclass()
# class Shops():
#     shopid: int
#     address:str
#     shopclass:str

# pizzashop = Shops(2, "karachi", "pizza shop")

# print(pizzashop)

@dataclass()
class accounts():
    name:str
    accounts_number:int
    accountstypse: str
    id: int

user1 = accounts("ahmed", 123456, "current", 1)
user2 = accounts("rizwan", 456789, "saving", 2)

print(user1)
print(user2)


