import sqlite3

#зададим соединение и т.п.
db_connection = sqlite3.connect('bot_database.db', check_same_thread=False)
db_cursor = db_connection.cursor()

def db_insert(table_name, column, value):
    db_cursor.execute(f'insert into {table_name}({column}) values ({value})')
    db_connection.commit()

def db_update(table_name, column, value, where_clause=''):
    db_cursor.execute(f'update {table_name} set {column} = {value} {where_clause}')
    db_connection.commit()

def db_select(select_clause):
    db_cursor.execute(select_clause)
    return db_cursor.fetchone()

def db_commit():
    db_connection.commit()

def delete_user(user_id):
    db_cursor.execute(f'delete from users_data where user_id = {user_id}')
    db_connection.commit()
    db_cursor.execute(f'delete from bot_questions where user_id = {user_id}')
    db_connection.commit()