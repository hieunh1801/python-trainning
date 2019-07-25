"""
    ***************
    Controller USER
    ***************
"""

# 3rd party library
from flask import Flask, jsonify, request, make_response, abort

# Personal Party
from config import db
from models.user import User, UserSchema
from controllers.status import *

fake_data_users = [
    {
        "address": "Thanh Oai - Ha Noi",
        "date_of_bird": "1998-01-18",
        "full_name": "Nguyen Van A",
        "id": 1,
        "id_manager": 2,
        "phone": "03432sdfasfd18555",
        "role": "admin",
        "username": "adminC",
        "password": "123456"
    },
    {
        "address": "Thanh Oai - Ha Noi",
        "date_of_bird": "1998-01-18",
        "full_name": "Nguyen Van A",
        "id": 2,
        "id_manager": 2,
        "phone": "0343218555",
        "role": "manager",
        "username": "managerA",
        "password": "123456"
    },
    {
        "address": "Viet Nam",
        "date_of_bird": "1998-01-18",
        "full_name": "Nguyen Van B",
        "id": 3,
        "id_manager": 2,
        "phone": "03223234",
        "role": "employee",
        "username": "employeeB",
        "password": "123456"
    },

]
"""
    - Admin 1: có tài nguyên 1
    - Manager 2: có tài nguyên 2
    - Employee 3: có tài nguyên 3
    - A1: share tài nguyên id=1 cho E3 để xem
"""
fake_data_user_resource = [
    {
        "id_user_resource_detail": 1,
        "id_user": 1,
        "id_resource": 1,
        "privilege": "owner",
    },
    {
        "id_user_resource_detail": 2,
        "id_user": 2,
        "id_resource": 2,
        "privilege": "owner"
    },
    {
        "id_user_resource_detail": 3,
        "id_user": 3,
        "id_resource": 3,
        "privilege": "owner"
    },
    {
        "id_user_resource_detail": 4,
        "id_user": 3,
        "id_resource": 1,
        "privilege": "view"
    },
]

fake_resource = [
    {
        "id_resource": 1,
        "table_name": "video",
        "id_table_mapping": 1,
        "role": "admin",
    },
    {
        "id_resource": 2,
        "table_name": "video",
        "id_table_mapping": 2,
        "role": "manager",
    },
    {
        "id_resource": 3,
        "table_name": "video",
        "id_table_mapping": 3,
        "role": "employee",
    },
    {
        "id_resource": 3,
        "table_name": "video",
        "id_table_mapping": 3,
        "role": "employee",
    },
    {
        "id_resource": 4,
        "table_name": "video",
        "id_table_mapping": 4,
        "role": "none",
    },
]


def get_all_user(page_number=1, page_size=20):
    """
    This function handle request: /api/user - GET
    with the complete lists of people

    :param id:          id of user to find
    :return:            json of array people
    """
    list_user = User.query.paginate(page_number, page_size, False).items
    schema = UserSchema(many=True)

    total_rows = User.query.order_by(User.user_id).count()
    data = schema.dump(list_user).data

    print("page numer and pagesize", page_number, page_size, data)
    return jsonify({"result": data, "total_rows": total_rows})


def create(user):
    """
    This function handle request: /api/user - POST
    create new user

    :return:            user
    """
    schema = UserSchema()
    new_user = schema.load(user, session=db.session).data

    # Step 1: Create dict of User
    if isinstance(new_user, str):
        print('new_user str', new_user)
    if isinstance(new_user, dict):
        usr_model = User()
        print('new_user dict', new_user)

        for k, v in new_user.items():
            usr_model.__dict__[k] = v
            print("  key :", k)
            print("  value :", v)

        new_user = usr_model
    else:
        print(" Request is not Dict ")
    print("request form", schema.dump(new_user).data)

    # Step 2: Check user exist
    is_exist_user_in_db = User.query.filter(
        User.username == user["username"]).one_or_none()
    if is_exist_user_in_db is None:
        db.session.add(new_user)
        db.session.commit()
        return schema.dump(new_user).data, HTTP_201_CREATED
    else:
        abort(HTTP_409_CONFLICT, "Username already exist {username}".format(
            username=user["username"]))


def get_one(username):
    """
    This function handle request: /api/user/{username} - GET

    :param id:          id of user to find
    :return:            user
    """
    schema = UserSchema()
    user = User.query.filter(User.username == username).one_or_none()
    print(user)
    # check user exist
    if user is not None:
        # Serialize the data for the response
        data = schema.dump(user).data
        print(data)
        return jsonify({"result": data})
    else:
        abort(HTTP_404_NOT_FOUND, f"User not found for: {username}")


def delete(username):
    """
    This function handle request: /api/user/{username} - DELETE

    :param username:    name of user to find
    :return:            user
    """
    for user in fake_data_users:
        print(user)
        if(user["id"] == id):
            fake_data_users.remove(user)
            return fake_data_users
    return "Not found"


def update(user):
    """
    This function handle request: /api/user/{id} - UPDATE

    :param user:        new user infomation
    :return:            array of user
    """
    for user_item in fake_data_users:
        print(user_item)
        if(user_item["id"] == id):
            fake_data_users.remove(user_item)
            fake_data_users.append(user)
            return fake_data_users
    return "Not found"


def login(account):
    """
    This function handle request: /api/login - PUT

    :param account:     have username && password to login
    :return:            array of user
    """
    # print(account)
    for user in fake_data_users:
        if(user["username"] == account["username"] and user["password"] == account["password"]):
            # return hash(user["username"])
            return user
    return "Login fail"


def logout():
    """
    This function handle request: /api/logout - GET

    :return:            Logout  
    """
    return "Logout Success"


def tree_user(id):
    """
    This function handle request: /api/user/tree_user/{id} - GET

    :return:            Logout  
    """
    schema = UserSchema(many=True)
    user_list = User.query.all()
    # Serialize the data for the response
    data = schema.dump(user_list).data

    return generate_tree_user_from_list_user(data)


def generate_tree_user_from_list_user(list_user):
    """
    Generate tree user from list user

    :return:            tree user  
    """
    user_tree = []
    for user in list_user:
        user["label"] = 0
    print(list_user)
    for user1 in list_user:
        if user1["superior_id"] is None and user1["label"] == 0:
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
    return user_tree
