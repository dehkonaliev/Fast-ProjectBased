from fastapi import FastAPI, HTTPException
from .schemas import PostCreate

app = FastAPI()

posts = {1: {"desc":"This is the post"}}

@app.get('/post/{id}')
def hello_world(id: int):
    if id not in posts:
        return HTTPException(status_code=404, detail="Post not found")
    return posts.get(id)


@app.post('/post')
def post_create(post: PostCreate) -> PostCreate:
    print(post.title, post.content)
    
    return post