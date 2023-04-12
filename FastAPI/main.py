# we need fastapi and uvicorn
# macos / linux - 'pip install PACKAGE_NAME'
# Windows - ???

from fastapi import FastAPI

# set up our API 
app = FastAPI()

# get ("/")
@app.get("/")
async def root():
    return {"message" : "Hey idiot" }

@app.get("/message")
async def display_message(msg: str):
    return f'Message was: {msg}.'

#return some JSON for our .NET app to deserialize
@app.get("/users")
async def get_users():
    # read the csv file and make each line a json object and return it
    with open('users.csv', 'r') as f:
        lines = f.readlines()
        users = []
        for line in lines:
            user = {}
            user['name'] = line.split(',')[0]
            user['age'] = int(line.split(',')[1].strip('\n'))
            users.append(user)
        return users


@app.get("/user")
async def get_user(name: str, age: int):
    return { "name" : name, "age" : age }
