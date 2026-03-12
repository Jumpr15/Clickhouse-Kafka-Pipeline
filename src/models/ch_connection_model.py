from pydantic import BaseModel

class CH_Config(BaseModel):
     host: str
     user: str
     password: str
     secure: bool
     query_limit: int
     