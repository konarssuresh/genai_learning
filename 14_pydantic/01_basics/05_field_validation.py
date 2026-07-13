from pydantic import BaseModel,field_validator,model_validator

class User(BaseModel):
    user_name:str 

    @field_validator('user_name')
    def user_name_length(cls,v):
        if len(v)<4:
            raise ValueError('Username must be atleast 4 chars')
        return v
    
class SignupData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def validate_passwords(cls,values):
        if values.password != values.confirm_password:
            raise ValueError("Passwords do not match")
        return values