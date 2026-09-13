from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

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



@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def html_home():
    return f"<h1>{posts[0]['title']}<h1>"


# @app.get("/")
# def home():
#     return {"message": "Hello FastAPI World!"}


@app.get("/api/posts")
def get_posts():
    return posts
