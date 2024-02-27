from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from models import *
from authentication import (hash_password)

#signals
from tortoise.signals import post_save
from tortoise import List,Optional,Type
from tortoise import BaseDBAsyncClient


app = FastAPI()

@post_save(User)
async def create_business (
    sender: "Type[User]",
    instance :User,
    created: bool,
    using_db :"Optional [BaseDBAsyncClient]",
    update_fields : List[str]
) -> None:
    if created:
        business_obj = await Business.create(
            business_name=instance.username, owner= instance
        )
        
        
@app.post('/user_registration')
async def user_registration(user:user_pydanticIn):
    user_info= user.dict(exclude_unset=True)
    user_info["password"] = hash_password(user_info)
    user_obj = await User.create(**user_info)
    new_user = await user_pydantic.from_tortoise_orm(user_obj)
    return {
        "status":"User Created Successfully",
        "data": f"Hello {new_user.username}, Thanks for choosing my services, check your email inbox and click on the link to confirm registration "
    }
    

@app.get('/')
def index():
    return {"message":"Me"}    

# registering the database with FastAPI
register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',  # Replace it with your DB URL!
    modules= { 'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True,
)
