# class User:
#     def __init__(self):
#         print("user is initializing")
#
# user_1 = User()
# user_1.height = 1.60
# user_1.id = "001"
# user_1.name = "é"
# print(f"{user_1.id} {user_1.height} {user_1.name}")

# def user(user_height, user_id, user_name):
#     ax = user_height
#     bx = user_id
#     cx = user_name
#     return f"{ax} {bx} {cx}"
#
# lol = user(1.7457454, 1, "é")
# print(lol)

class User:
    def __init__(self, user_height, user_id, user_name):
        self.height = user_height
        self.id = user_id
        self.name = user_name

me = User(user_id = 1, user_height = 1.7457454, user_name = "é")


print(f"{me.height} {me.id} {me.name}")

