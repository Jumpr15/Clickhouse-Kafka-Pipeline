import os
from dotenv import load_dotenv
load_dotenv()

row1 = [10, 'String Value 10', 5.]
row2 = [20, 'String Value 20', -10.]
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

client = CH_Client(ch_config)
client.create_table(
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
     ]
)