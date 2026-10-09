from pydantic import BaseModel

class Student(BaseModel):

    name:str

new_student={"name":"aneesh"}

student=Student(**new_student)

print(type(student))