from dotenv import load_dotenv
import os
import clickhouse_connect

from models.ch_connection_model import CH_Config

load_dotenv()

class CH_Client:
    def __init__(self, ch_config: CH_Config):
        self.client = clickhouse_connect.get_client(
            **ch_config.model_dump()
        )

    def create_table(self, table_name, keys: list[dict]):
        key_list = ", ".join(f"{key['name']} {key['type']}" for key in keys)
        
        try:
            check_table_statement = f"EXISTS {table_name}"
            if not self.client.command(  
                check_table_statement
            ):
                create_table_statement = f'CREATE TABLE {table_name} ({key_list}) ENGINE = MergeTree() ORDER BY key'
                res = self.client.command(
                    create_table_statement
                )
                return res
        
        except Exception as e:
            print(e)
    

    # client.insert('new_table', data, column_names=['key', 'value', 'metric'])
    # print(client.command('EXISTS new_table'))
    
    # client.close()
    
    