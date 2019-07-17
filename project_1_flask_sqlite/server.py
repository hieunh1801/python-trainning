import psycopg2
from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "112297607",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "dvdrental")
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")
    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
# finally:
#     #closing database connection.
#         if(connection):
#             cursor.close()
#             connection.close()
#             print("PostgreSQL connection is closed")


# Get All Actor
def get_all_actor():
    query_select_allactor = """
    select * from actor
    """
    cursor.execute(query_select_allactor)
    list_actors = cursor.fetchall()
    return jsonify(list_actors)

# Insert New Actor
def insert_new_actor(first_name = "default first_name", last_name = "default last_name", last_update = datetime.datetime.now()):
    query = f"""
    insert into actor(first_name, last_name, last_update) 
    values('{str(first_name)}', '{str(last_name)}', '{str(last_update)}');
    """
    cursor.execute(query)
    connection.commit()

# Update actor
def update_actor_by_id(
        actor_id,
        first_name = "default first_name",
        last_name = "default last_name",
        last_update = datetime.datetime.now()):
    query = f"""
    UPDATE public.actor
	SET first_name='{first_name}', last_name='{last_name}', last_update='{last_update}'
	WHERE actor_id={actor_id};
    """
    cursor.execute(query)
    connection.commit()

# Get Actor by id
def get_actor_by_id(actor_id):
    query = f'select * from actor where actor_id = {actor_id}'
    cursor.execute(query)
    list_actors = cursor.fetchall()
    return jsonify(list_actors)

@app.route('/actor', methods=['GET', 'POST', 'PUT'])
def actor():
    if request.method == 'GET':
        print('Get - Request: ', request)
        return get_all_actor()
    elif request.method == 'POST':
        print('Post - Request: ',request)
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        insert_new_actor(first_name, last_name, datetime.datetime.now())
        return 'POST SUCCESS'
    elif request.method == 'PUT':
        print('PUT - Request', request)
        actor_id = request.form['actor_id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        update_actor_by_id(actor_id, first_name,last_name)
        return 'PUT SUCCESS'
    return get_all_actor()


@app.route('/actor/<actor_id>')
def actor_id(actor_id):
    return get_actor_by_id(actor_id)


if __name__ == '__main__':
    app.run(debug=True)