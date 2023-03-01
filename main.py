from typing import Union
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from models import *
from authentaction import *
#signal
from tortoise.signals import post_save
from typing import List,Optional,Type
from tortoise import BaseDBAsyncClient

app = FastAPI()


'''
Arguments sent with this signal:

sender
The model class.
instance
The actual instance being saved.
created
A boolean; True if a new record was created.
raw
A boolean; True if the model is saved exactly as presented (i.e. when loading a fixture). One should not query/modify other records in the database as the database might not be in a consistent state yet.
using
The database alias being used.
update_fields
The set of fields to update as passed to Model.save(), or None if update_fields wasn’t passed to save().

'''

@post_save(User)
async def create_business(
    sender:'Type[User]',
    instance: User,
    created: bool,
    using_db :"Optional[BaseDBAsyncClient]",
    update_fields : List[str]
) -> None:
    if created:
        business_obj = await Business.create(
            business_name = instance.username, owner = instance
        )

        await business_pydantic.from_tortoise_orm(business_obj)
        #send the email
        
#What is Async and Await do?
#Use of async and await enables the use of ordinary try / catch blocks around asynchronous code. Note: The await keyword is only valid inside async functions within

@app.post('/registration')
async def user_registration(user:user_pydanticIn):
    user_info = user.dict(exclude_unset = True)
    user_info["password"] = get_hashed_password(user_info['password'])  # this will make the password hashed 
    user_obj = await User.create(**user_info)
    new_user = await user_pydantic.from_tortoise_orm(user_obj)         # this will create user boj into pydantic model 
    return {
        "status":'Ok',
        "data" : f"Hello {new_user.username}, thank for choosing our services. please check your email inbox and click on the link to confirm your registration"
    }



@app.get("/")
def index():
    return {"Message": "Hi Vishal"}

register_tortoise(
    app,
    db_url="sqlite://database.sqlite3",
    modules= {"models":["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
