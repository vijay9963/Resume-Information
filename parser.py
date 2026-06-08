from pydantic import BaseModel
from typing import List, Union
import json

class ResumeInfo(BaseModel):
    name: str
    email: str
    phone: str
    skills: List[str]
    total_experience_years: Union[int, str]

def parse_response(response):

    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    data = json.loads(response)

    return ResumeInfo(**data)