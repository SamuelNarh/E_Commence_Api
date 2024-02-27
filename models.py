from tortoise import Model,fields #From  Tortoise ORM
import datetime
from pydantic import BaseModel
from datetime import datetime
from tortoise.contrib.pydantic import pydamtic_model_creator

class User(Model):
    id = fields.Intfield(pk=True ,index=True)
    username= fields.CharField(max_length=20, nul =False, unique =True )
    email = fields.CharField(max_length=200, null =False ,unique = True)
    password = fields.CharField(max_length=100 , null=False)
    is_verified = fields.BooleanField(default = False)
    join_date = fields.DatetimeField(default = datetime.utcnow)


class Business(Model):
    id = fields.IntField(pk=True, index=True)
    business_name = fields.CharField(max_length=20,null=False,unique=True)
    city = fields.CharField(max_length=100, null= False, default ="unspecified")
    region = fields.CharField(max_length=100,null=False,default="Unspecified")
    business_descriptioin =  fields.TextField(null=True)
    logo = fields.CharField(max_length=200,null=False, default='default.jpg')
    owner = fields.ForeignKeyField("models.User", related_name="business")
    
class Product (Model):
    id = fields.IntField(pk=True , index =True)
    name = fields.CharField(max_length=100, null= False , index = True)
    category = fields.CharField( max_length=50 , index = True)
    original_price = fields.DecimalField(max_digits=12,decimal_places=2)
    new_prices = fields.DecimalField(max_digits=12,decimal_places=2)
    percentage_discount = fields.IntField()
    offer_expiration_date = fields.DateField(default=datetime.utcnow)
    product_image = fields.CharField(max_length=200 ,null = False , default="productDefault.jpg")
    business = fields.ForeignKeyField("models.Business",related_name="products")
    
    
#Create pydantic Models

user_pydantic = pydamtic_model_creator (User , name ="User" ,exclude=("is verified", ))
user_pydanticIn = pydamtic_model_creator(User , name ="UserIn"  , exclude_readonly=True) #Obtain user data from frontend
user_pydanticOut = pydamtic_model_creator


