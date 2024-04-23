from fastapi import FastAPI, Request, Form
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware


app=FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

app.add_middleware(SessionMiddleware, secret_key="secret_key")


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})

@app.post("/signin")
def signin(request: Request, username: str=Form(default=None), password: str=Form(default=None)):
    if not username or not password:
        return templates.TemplateResponse("emptyerrorpage.html", {"request": request})
    if username == "test" and password == "test":
        request.session["SIGNED_IN"] = True
        return RedirectResponse(url="/member",status_code=303) #引導使用get方法
    else:
        return templates.TemplateResponse("errorpage.html", {"request": request})


@app.get("/member")
def member(request: Request):
    if request.session.get("SIGNED_IN"):
        return templates.TemplateResponse("member.html", {"request": request})
    else:
        return RedirectResponse(url="/")

@app.get("/errorpage")
def errorpage(request: Request):
    return templates.TemplateResponse("errorpage.html", {"request": request})

@app.get("/emptyerrorpage")
def emptyerrorpage(request: Request):
    return templates.TemplateResponse("emptyerrorpage.html", {"request": request})

@app.get("/signout")
def signout(request: Request):
    request.session["SIGNED_IN"] = False
    return RedirectResponse(url="/")




if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)