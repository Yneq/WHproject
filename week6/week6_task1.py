from fastapi import FastAPI, Request, Form, Query, Depends
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
import mysql.connector



app=FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
app.add_middleware(SessionMiddleware, secret_key="secret_key")



def get_db():
    try:
        db = mysql.connector.connect(
            user="root",
            password="244466666",
            host="localhost",
            database="website"
        )
        yield db
    finally:
        db.close()

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})

@app.post("/signup")
def signin(username: str=Form(default=None),password: str=Form(default=None), name: str=Form(default=None), db: mysql.connector.MySQLConnection = Depends(get_db)):
    if not username or not password or not name:
        return RedirectResponse(url="/error?message=請輸入必要欄位", status_code=303)
    
    cursor = db.cursor()
    try:
        cursor.execute("SELECT name FROM member WHERE username=%s", (username,))
        if cursor.fetchone():
            return RedirectResponse(url="/error?message=帳號已經被註冊", status_code=303)

        cursor.execute("INSERT INTO member(username, password, name) VALUES (%s, %s, %s)", (username, password, name))
        db.commit()
    finally:
        cursor.close()
    return RedirectResponse(url="/", status_code=303)

@app.post("/signin")
def signin(request: Request, username: str=Form(default=None),password: str=Form(default=None), name: str=Form(default=None), db: mysql.connector.MySQLConnection = Depends(get_db)):
    if not username or not password:
        return RedirectResponse(url="/error?message=請輸入必要欄位", status_code=303)
    
    cursor = db.cursor()
    try:
        cursor.execute("SELECT id, name FROM member WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        if user:
            user_id, user_name = user
            request.session["SIGNED_IN"] = True
            request.session["username"] = username
            request.session["name"] = user_name
            request.session["member_id"] = user_id
            return  RedirectResponse(url="/member", status_code=303)
        else:
            return RedirectResponse(url="/error?message=帳號或密碼輸入錯誤", status_code=303)
    finally:
        cursor.close()

@app.get("/member")
def member(request: Request, db: mysql.connector.MySQLConnection = Depends(get_db)):
    if request.session.get("SIGNED_IN"):
        cursor = db.cursor(dictionary=True)
        cursor.execute("""
        SELECT member.name, message.content FROM member
        INNER JOIN message ON member.id = message.member_id
        ORDER BY message.id DESC            
        """)
        messages = cursor.fetchall()
        cursor.close()
        name=request.session.get("name")
        return templates.TemplateResponse("member.html", {"request": request,"message": name, "messages": messages, "name":request.session.get("name")})
    else:
        return RedirectResponse(url="/")

@app.get("/error")
def error(request: Request, message: str=Query(None)):
    return templates.TemplateResponse("error.html", {"request": request, "message": message})

@app.get("/signout")
def signout(request: Request):
    request.session["SIGNED_IN"] = False
    return RedirectResponse(url="/")

@app.post("/creatMessage")
def creat_message(request: Request, content: str = Form(...), db: mysql.connector.MySQLConnection = Depends(get_db)):
    member_id = request.session.get("member_id")
    if not member_id:
        return RedirectResponse(url="/login", status_code=303)

    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO message(member_id, content) VALUES (%s, %s)", (member_id, content))
        db.commit()
    finally:
        cursor.close()
    return RedirectResponse(url="/member", status_code=303)


    

if __name__ == "__main__":
    uvicorn.run(app="week6_task1:app", reload=True)