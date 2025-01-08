from pydantic import BaseModel

class StatusSchema(BaseModel):
    status: str = "ok"
    code: int = 200
