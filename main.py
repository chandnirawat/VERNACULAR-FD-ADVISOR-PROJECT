from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from auth import register_user, login_user
from recommendation import recommend_fd
from chatbot import chatbot_reply
from translator import to_hindi

app = FastAPI()
templates = Jinja2Templates(directory="templates")

current_user = None

# 🔐 Login Page
@app.get("/", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


# 🔐 Login
@app.post("/login", response_class=HTMLResponse)
def login(request: Request, username: str = Form(...), password: str = Form(...)):
    global current_user
    if login_user(username, password):
        current_user = username
        return templates.TemplateResponse("dashboard.html", {"request": request})
    return HTMLResponse("Login Failed")


# 📝 Register Page
@app.get("/register", response_class=HTMLResponse)
def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


# 📝 Register
@app.post("/register", response_class=HTMLResponse)
def register(request: Request, username: str = Form(...), password: str = Form(...)):
    if register_user(username, password):
        return HTMLResponse("Registered! Go to login.")
    return HTMLResponse("User already exists")


# 💰 FD Recommendation
@app.post("/recommend", response_class=HTMLResponse)
def recommend(request: Request,
              amount: float = Form(...),
              duration: int = Form(...),
              risk: str = Form(...),
              language: str = Form(...)):

    result = recommend_fd(amount, duration, risk)

    text = f"Bank: {result['bank']} | Interest: ₹{round(result['interest'],2)}"

    if language == "hindi":
        text = to_hindi(text)

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "result": text
    })


# 🤖 Chatbot (FIXED - only ONE route)
@app.post("/chat", response_class=HTMLResponse)
def chat(request: Request, message: str = Form(...)):
    reply = chatbot_reply(message)

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "chat_reply": reply
    })

@app.post("/login", response_class=HTMLResponse)
def login(request: Request, username: str = Form(...), password: str = Form(...)):
    return templates.TemplateResponse("dashboard.html", {"request": request})