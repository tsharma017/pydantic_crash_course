from pydantic import BaseModel


class Address(BaseModel):
    city: str
    state: str
    pin:str
    
class Patient(BaseModel):
    
    name: str
    gender: str
    age: int
    address: Address
    
addres_dict = {'city': 'Baglung', 'state': 'Gandaki', 'pin': '14200'}
    
address1 = Address(**addres_dict)
    
patient_dict = {'name': 'Tej', 'gender': 'male', 'age': 34, 'address': address1}
    
patient1 = Patient(**patient_dict)
    
temp = patient1.model_dump()

print(temp)
print(type(temp))


