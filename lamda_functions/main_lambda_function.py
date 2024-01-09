import os
import json
import pymysql
import requests
import boto3

db_host = os.getenv('host')
db_user = os.getenv('user')
db_password = os.getenv('password')
db_name = os.getenv('db_name')

def lambda_handler(event, context):

    api_url = 'http://api.open-notify.org/iss-now.json'

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            latitude = data['iss_position']['latitude']
            longitude = data['iss_position']['longitude']
            timestamp = data['timestamp']

            store_data_in_rds(latitude, longitude, timestamp)

            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Data fetched and stored in RDS successfully'})
            }
        else:
            return {
                'statusCode': response.status_code,
                'body': json.dumps({'error': 'Failed to fetch data from the API'})
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Failed to store data'})
        }

def store_data_in_rds(latitude, longitude, timestamp):
    connection = pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name,
        port=3306,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            table_name = 'data'
            create_table_sql = f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    latitude DECIMAL(9,6),
                    longitude DECIMAL(9,6),
                    timestamp INT
                )
            """
            cursor.execute(create_table_sql)

            insert_sql = f"INSERT INTO {table_name} (latitude, longitude, timestamp) VALUES (%s, %s, %s)"
            cursor.execute(insert_sql, (latitude, longitude, timestamp))

            connection.commit()

    finally:
        connection.close()

