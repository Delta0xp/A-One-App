from pydantic import BaseModel
from typing import Optional

class DoctorCreate(BaseModel):
    name: str
    specialty: str
    bio: Optional[str] = None
    image_url: Optional[str] = None

class DoctorResponse(DoctorCreate):
    id: int

    class Config:
        orm_mode = True
