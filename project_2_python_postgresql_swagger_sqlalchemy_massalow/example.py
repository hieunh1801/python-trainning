"""
    Python Dictionary
"""
from pprint import pprint
from copy import copy, deepcopy
null = -1
list_user = [
   {
      "address": "address",
      "dob": "1998-01-18",
      "email": "admin@gmail.com                                   ",
      "fullname": "admin full nam",
      "password": "123456                          ",
      "phonenumber": "123456789      ",
      "role": "admin",
      "superior_id": null,
      "user_id": 1,
      "username": "admin                           "
   },
   {
      "address": "string",
      "dob": null,
      "email": "string                                            ",
      "fullname": "string",
      "password": "string                          ",
      "phonenumber": "string         ",
      "role": "admin",
      "superior_id": 0,
      "user_id": 0,
      "username": "string                          "
   },
   {
      "address": "string",
      "dob": null,
      "email": "string                                            ",
      "fullname": "string",
      "password": "string                          ",
      "phonenumber": "string         ",
      "role": "manager",
      "superior_id": 1,
      "user_id": 2,
      "username": "manager1                        "
   },
   {
      "address": "string",
      "dob": null,
      "email": "string                                            ",
      "fullname": "string",
      "password": "string                          ",
      "phonenumber": "string         ",
      "role": "manager",
      "superior_id": 1,
      "user_id": 3,
      "username": "manager2                        "
   },
   {
      "address": "string",
      "dob": null,
      "email": "string                                            ",
      "fullname": "string",
      "password": "string                          ",
      "phonenumber": "string         ",
      "role": "manager",
      "superior_id": 1,
      "user_id": 4,
      "username": "manager3                        "
   },
   {
      "address": "string",
      "dob": null,
      "email": "string                                            ",
      "fullname": "string",
      "password": "string                          ",
      "phonenumber": "string         ",
      "role": "manager",
      "superior_id": 1,
      "user_id": 5,
      "username": "manager4                        "
   },
   {
      "address": "string",
      "dob": null,
      "email": "string                                            ",
      "fullname": "string",
      "password": "string                          ",
      "phonenumber": "string         ",
      "role": "manager",
      "superior_id": 2,
      "user_id": 6,
      "username": "em1.1                           "
   },
   {
      "address": "string",
      "dob": null,
      "email": "string                                            ",
      "fullname": "string",
      "password": "string                          ",
      "phonenumber": "string         ",
      "role": "manager",
      "superior_id": 2,
      "user_id": 7,
      "username": "em1.2                           "
   },
   {
      "address": "string",
      "dob": null,
      "email": "string                                            ",
      "fullname": "string",
      "password": "string                          ",
      "phonenumber": "string         ",
      "role": "manager",
      "superior_id": 2,
      "user_id": 8,
      "username": "em1.3                           "
   },
   {
      "address": "string",
      "dob": null,
      "email": "string                                            ",
      "fullname": "string",
      "password": "string                          ",
      "phonenumber": "string         ",
      "role": "manager",
      "superior_id": 2,
      "user_id": 9,
      "username": "em1.4                           "
   },
   {
      "address": "string",
      "dob": null,
      "email": "string                                            ",
      "fullname": "string",
      "password": "string                          ",
      "phonenumber": "string         ",
      "role": "manager",
      "superior_id": 2,
      "user_id": 10,
      "username": "em1.5                           "
   },
   {
      "address": "string",
      "dob": null,
      "email": "string                                            ",
      "fullname": "string",
      "password": "string                          ",
      "phonenumber": "string         ",
      "role": "manager",
      "superior_id": 2,
      "user_id": 11,
      "username": "em1.6                           "
   },
   {
      "address": "string",
      "dob": null,
      "email": "string                                            ",
      "fullname": "string",
      "password": "string                          ",
      "phonenumber": "string         ",
      "role": "manager",
      "superior_id": 3,
      "user_id": 12,
      "username": "em2.1                           "
   },
   {
      "address": "string",
      "dob": null,
      "email": "string                                            ",
      "fullname": "string",
      "password": "string                          ",
      "phonenumber": "string         ",
      "role": "manager",
      "superior_id": 3,
      "user_id": 13,
      "username": "em2.2                           "
   },
   {
      "address": "string",
      "dob": null,
      "email": "string                                            ",
      "fullname": "string",
      "password": "string                          ",
      "phonenumber": "string         ",
      "role": "manager",
      "superior_id": 3,
      "user_id": 14,
      "username": "em2.3                           "
   },
   {
      "address": "string",
      "dob": null,
      "email": "string                                            ",
      "fullname": "string",
      "password": "string                          ",
      "phonenumber": "string         ",
      "role": "manager",
      "superior_id": 3,
      "user_id": 15,
      "username": "em2.4                           "
   },
   {
      "address": "string",
      "dob": null,
      "email": "string                                            ",
      "fullname": "string",
      "password": "string                          ",
      "phonenumber": "string         ",
      "role": "manager",
      "superior_id": 3,
      "user_id": 16,
      "username": "em2.5                           "
   },
   {
      "address": "string",
      "dob": null,
      "email": "string                                            ",
      "fullname": "string",
      "password": "string                          ",
      "phonenumber": "string         ",
      "role": "manager",
      "superior_id": 3,
      "user_id": 17,
      "username": "em2.6                           "
   },
   {
      "address": "string",
      "dob": null,
      "email": "string                                            ",
      "fullname": "string",
      "password": "string                          ",
      "phonenumber": "string         ",
      "role": "manager",
      "superior_id": 3,
      "user_id": 18,
      "username": "em2.7                           "
   },
   {
      "address": "string",
      "dob": null,
      "email": "string                                            ",
      "fullname": "string",
      "password": "string                          ",
      "phonenumber": "string         ",
      "role": "manager",
      "superior_id": 3,
      "user_id": 19,
      "username": "em2.8                           "
   },
   {
      "address": "string",
      "dob": null,
      "email": "string                                            ",
      "fullname": "string",
      "password": "string                          ",
      "phonenumber": "string         ",
      "role": "admin",
      "superior_id": null,
      "user_id": 20,
      "username": "admin2                          "
   }
]
user_tree = []
a = {"name": "Hieu"}
a["age"] = []
a["age"].append({"a": "a"})
print(a)


# Step 1: assign label to user
for user in list_user:
    user["label"] = 0

# Step 2: Find fist node in tree
for user1 in list_user:
   if user1["superior_id"] == null and user1["label"] == 0:
      user1["label"] = 1
      user1["subordinate"] = []
      for user2 in list_user:
         if user2["label"] == 0 and user2["superior_id"] == user1["user_id"]:
            user2["label"] = 1
            user2["subordinate"] = []
            for user3 in list_user:
               if user3["label"] == 0 and user3["superior_id"] == user2["user_id"]:
                  user2["subordinate"].append(user3)
            user1["subordinate"].append(user2)
         user_tree.append(user1)

pprint(user_tree)
