import uuid
from datetime import date, datetime, timedelta
from typing import Literal
from pydantic import BaseModel, confloat, validator, field_validator
from enums import DepartmentEnum


#Creating Basemodel class which is pydantic model
class Module(BaseModel):
    id: int | uuid.UUID
    name: str
    professor: str
    credits: Literal[10, 20]
    registration_code: str


class Student(BaseModel):
    id: uuid.UUID
    name: str
    date_of_birth: date
    GPA: confloat(ge=0, le=4) #float
    course: str | None #Union[int, None]
    department: DepartmentEnum #str
    fees_paid: bool
    modules: list[Module] = []


    @field_validator('modules')
    def validate_module_length(cls, value):
        if len(value) and len(value) != 3:
            raise ValueError('List of modules should have length 3')
        return value


    # @validator('date_of_birth')
    @field_validator('date_of_birth')
    def sixteen_or_above(cls, value):
        sixteen_years_ago = datetime.now() - timedelta(days=365*16)

        # convert datetime object -> date
        sixteen_years_ago = sixteen_years_ago.date()
        
        # raise error if DOB is more recent than 16 years past.
        if value > sixteen_years_ago:
            raise ValueError("Too young to enrol, sorry!")
        return value
    
