"""
    ***************
    Controller USER
    ***************
"""

# 3rd party library
from flask import Flask, jsonify, request

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

    :param id:          id of user to find
    :return:            user
    """

    print("page numer and pagesize", page_number, page_size)
    return fake_data_users


def create(user):
    """
    This function handle request: /api/user - POST

    :param id:          id of user to find
    :return:            user
    """
    print("request form", user)
    fake_data_users.append(user)
    return fake_data_users


def get_one(id):
    """
    This function handle request: /api/user/{id} - GET

    :param id:          id of user to find
    :return:            user
    """
    for user in fake_data_users:
        print(user)
        if(user["id"] == id):
            return user
    return "Not found"


def delete(id):
    """
    This function handle request: /api/user/{id} - DELETE

    :param id:          id of user to find
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
