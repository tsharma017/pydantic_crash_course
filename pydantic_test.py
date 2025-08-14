from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    
    name: Annotated[str, Field(max_length=50, title = 'Namf of patient', description= 'Description of patient', examples= ['Raj', 'Amit'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt = 0, lt = 120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    height: Annotated[float, Field(gt=0)]  
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]
    allergies: Optional[List[str]] = Field(max_length=10)
    contact_details: Dict[str, str]
     
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        
        valid_domains = ['hdfc.com', 'icici.com']
        
        #abc@gmail.com
        domain_name = value.split('@')[-1]
        
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        
        return value
    
    @field_validator('name') # field validator will help to change name to capital 
    @classmethod # fild validator work in two mode: before mode and after mode 
    def transfrom_name(cls, value): # mode = after is default 
        return value.upper()
    
    @field_validator('age', mode = 'after')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')
        
    @model_validator(mode='after') # Add some addtional information
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emegency' not in model.contact_details:
            raise ValueError('patients older than 60 must have an emergency contact')
        return model
    
    @computed_field(return_type=float)
    def bmi(self) -> float:    # ← expose as patient.bmi
        return round(self.weight / (self.height ** 2), 2)
    
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('BMI', patient.bmi)
    print('Inserted into database')
    


patient_info = {
    'name': 'Tej',
    'email': 'abc@hdfc.com',
    'linkedin_url': 'https://linkedin.com/in/1322',
    'age': 30,                     # string '30' would also coerce, but int is cleaner
    'height': 1.5,
    'weight': 75.2,
    'married': True,               # 1 would coerce to True
    'allergies': ['Pollen', 'Dust'],
    'contact_details': {'phone': '6462887216', 'emergency': '23456'}
}

patient1 = Patient(**patient_info) # validation –> type coercion

insert_patient_data(patient1)

# computed field