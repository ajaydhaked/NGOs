from header import *

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "page": "home"})

@app.get("/signup")
def v_signup(request: Request,message: str = None):
    return templates.TemplateResponse("signup.html", {"request": request,"message":message})


@app.get("/login")
def v_login(request: Request,message: str = None):
    return templates.TemplateResponse("login.html", {"request": request,"message":message})





@app.post("/signup")
async def signup(request: Request):
    data = await request.json()
    # if data['type'] == 'organiser':
    #     user = Organiser_l(**data)
    #     temp = checkfororganiser(user)
    #     if temp == 1:
    #         return {"message": "Username already exists", "status": 0}
    #     elif temp == 2:
    #         return {"message": "Roll number already exists", "status": 0}
    #     elif temp == 3:
    #         return {"message": "Enrollment key does not exist", "status": 0}
    #     register_organizer(user.name,user.roll_no,user.username,user.password,False,user.enrollment_key)
    #     return {"message": "Signup successful", "status": 1,"token":user.username}
    # elif data['type'] == 'student':
    #     user = Student_l(**data)
    #     temp = checkforstudent(user)
    #     if temp == 1:
    #         return {"message": "Username already exists", "status": 0}
    #     elif temp == 2:
    #         return {"message": "Roll number already exists", "status": 0}
    #     register_student(user.name,user.roll_no,user.username,user.password,True)
    #     return {"message": "Signup successful", "status": 1,"token":user.username}
    # elif data['type'] == 'outsider':
    #     user = Outsider_l(**data)
    #     temp = checkforoutsider(user)
    #     if temp == 1:
    #         return {"message": "Username already exists", "status": 0}
    #     register_outsider(user.name,user.username,user.password,user.college)
    #     allocate_outsider_to_hall(user.username)
    #     return {"message": "Signup successful", "status": 1,"token":user.username}
    # else:
    #     return {"message": "Invalid user type", "status": 0}
    print(data)
    user = SignUp_l(**data)
    print(user)
    return {"message": "Signup successful", "status": 1,"token":user.username}  


@app.post("/login")
async def login(user: User_l):
    print(user)
    if user == 1:
        return {"message": "Invalid username or password", "status": 0}
    else:
        return {"message": "Login successful", "status": 1,"token":user.username}
