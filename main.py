from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


posts: list[dict] = [
{
"id" : 1,
"author": "Dev DKP",
"title": "FastAPI is Amazing",
"content": "This framework is indeed super easy, cool and super fast.",
"date_posted": "September 12, 2026"
},
{
"id" : 2,
"author": "Devendra DKP",
"title": "Python is Great for Web Development",
"content": "Python is a great language for web development, and FastAPI makes it even better.",
"date_posted": "September 13, 2026"
}
]



@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def html_home(request: Request):
    return templates.TemplateResponse(
        request,
        "home.html",
        {"posts": posts, "title": "Home"}, 
    )



@app.get("/api/posts")
def get_posts():
    return posts
