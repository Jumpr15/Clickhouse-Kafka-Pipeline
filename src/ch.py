import os
from dotenv import load_dotenv
load_dotenv()

row1 = ["key1", 81]
row2 = ["key2", 24]
data = [row1, row2]

from models.ch_connection_model import CH_Config

from ch_connection import CH_Client

ch_config = CH_Config(
     host=os.getenv("HOSTNAME"),
     user=os.getenv("USERNAME"),
     password=os.getenv("PASSWORD"),
     secure=True,
     query_limit=5
)

ch = CH_Client(ch_config)
ch.create_table(
     "example_table",
     [
          {
               "name": "key",
               "type": "String",
          },
          {
               "name": "key_age",
               "type": "Int32"
          }
     ],
     'key'
)

ch.client.insert("example_table", data, column_names=['key', 'key_age'])