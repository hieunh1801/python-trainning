"""
    ***************
    Controller RESOURCE
    ***************
"""
# 3rd party library
from flask import Flask, jsonify, request

# Personal
from controllers.user import fake_data_user_resource, fake_data_users, fake_resource
fake_data_users = [
    {
        "address": "Thanh Oai - Ha Noi",
        "date_of_bird": "1998-01-18",
        "full_name": "Nguyen Van A",
        "id": 1,
        "id_manager": 2,
        "phone": "03432sdfasfd18555",
        "role": 1,
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
        "role": 2,
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
        "role": 3,
        "username": "employeeB",
        "password": "123456"
    },

]
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
        "role": 1,
    },
    {
        "id_resource": 2,
        "table_name": "video",
        "id_table_mapping": 2,
        "role": 2,
    },
    {
        "id_resource": 3,
        "table_name": "video",
        "id_table_mapping": 3,
        "role": 3,
    },
    {
        "id_resource": 3,
        "table_name": "video",
        "id_table_mapping": 3,
        "role": 3,
    },
    {
        "id_resource": 4,
        "table_name": "video",
        "id_table_mapping": 4,
        "role": 10,
    },
]


def removeDuplicateInArray(list):
    id_resource_list = set()
    new_list = []
    for obj in list:
        if obj["id_resource"] not in id_resource_list:
            new_list.append(obj)
            id_resource_list.add(obj["id_resource"])
    return new_list


def get_all_resource(account):
    """
    This function handle request: /api/resouce - GET

    :account:          account
    :return:           array of resource
    """
    current_id_user = -1
    current_role = "None"
    # Check user exsit
    for user in fake_data_users:
        if (user["username"] == account["username"] and user["password"] == account["password"]):
            current_id_user = user["id"]
            current_role = user["role"]
    # If not found => return fail
    if(current_id_user == -1):
        return "Login fail"

    array_resouce = []  # list resource to get
    # get from resouce
    for resource in fake_resource:
        if (current_role < resource["role"]):
            array_resouce.append(
                {
                    "id_resource": resource["id_resource"],
                    "privilege": "edit"
                }
            )
    # get from user_resouce
    for item in fake_data_user_resource:
        if(current_id_user == item["id_user"]):
            array_resouce.append(
                {
                    "id_resource": item["id_resource"],
                    "privilege": item["privilege"]
                }
            )
    return removeDuplicateInArray(array_resouce)
