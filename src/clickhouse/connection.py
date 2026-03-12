from dotenv import load_dotenv
import os

load_dotenv()

import clickhouse_connect

row1 = [1000, 'String Value 1000', 5.233]
row2 = [2000, 'String Value 2000', -107.04]
data = [row1, row2]

if __name__ == '__main__':
    client = clickhouse_connect.get_client(
        host=os.getenv("HOSTNAME"),
        user=os.getenv("USERNAME"),
        password=os.getenv("PASSWORD"),
        secure=True
    )
    
    client.create('CREATE TABLE new_table (key UInt32, value String, metric Float64) ENGINE MergeTree ORDER BY key')
    
    