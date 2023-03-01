from tortoise.models import Model     #Tortoise ORM is an easy-to-use asyncio ORM (Object Relational Mapper) inspired by Django.
from tortoise import fields
from pydantic import BaseModel    #Data validation and settings management using Python type annotations.pydantic enforces type hints at runtime, and provides user friendly errors when data is invalid.Define how data should be in pure, canonical Python; validate it with pydantic.
from datetime import datetime
from tortoise.contrib.pydantic import pydantic_model_creator



class User(Model):
    id = fields.IntField(pk=True,index=True)
    username = fields.CharField(max_length=20,null=False,unique = True)
    email = fields.CharField(max_length=200,unique=True,null=False)
    password = fields.CharField(max_length=100,null=False)
    is_varified = fields.BooleanField(default=False)
    join_date = fields.DatetimeField(default = datetime.utcnow)



class Business(Model):
    id = fields.IntField(pk=True,index=True)
    business_name = fields.CharField(max_length=500,null=False,unique = True)
    city = fields.CharField(max_length=100,null = False,default = 'Unspecified')
    region = fields.CharField(max_length=100,null = False,default = 'Unspecified')
    business_description = fields.TextField(null = True,default = 'Unspecified')
    logo = fields.CharField(max_length=200,null=False,default='default.jpeg')
    owner = fields.ForeignKeyField("models.User",related_name='business')


class Product(Model):
    id = fields.IntField(pk=True,index=True)
    name = fields.CharField(max_length=100,null=False,index=True)
    category = fields.CharField(max_length=30,index=True)
    original_price = fields.DecimalField(max_digits=12,decimal_places=2)
    new_price = fields.DecimalField(max_digits=12,decimal_places=2)
    percentage_discount = fields.IntField()
    offer_expiration_date = fields.DatetimeField(default = datetime.utcnow)
    Product_image = fields.CharField(max_length=200,null=False,default='product_default.jpeg')
    business = fields.ForeignKeyField("models.Business",related_name='products')


user_pydantic =pydantic_model_creator(User, name = 'User', exclude =("is_varified", ) )
user_pydanticIn = pydantic_model_creator(User, name="UserIn",exclude_readonly = True,exclude =("is_varified","join_date") )     
user_pydanticOut = pydantic_model_creator(User,name="UserOut",exclude = ('password', ))


business_pydantic = pydantic_model_creator(Business,name='Business')
business_pydanticIn = pydantic_model_creator(Business,name='BusinessIn',exclude_readonly = True)  #foregin key

product_pydantic = pydantic_model_creator(Product,name='Product')
product_pydanticIn = pydantic_model_creator(Product,name='ProductIn',exclude=("percentage_discount","id"))