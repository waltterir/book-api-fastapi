from fastapi import HTTPException, Response , status
from .models import AuthorBase, AuthorOut

auths = [
    {"id": 0, "name": "Sofi Oksanen"},
    {"id": 1, "name": "Vares"},
    {"id": 2, "name": "RR Martin"},
]

def get_authors(author: str):
    if author == "":
        return auths
    else: 
        return [a for a in auths if a["name"] == author]

def create_new_author(auth_in: AuthorBase):
    new_id = auths[-1]["id"]+1
    auth = AuthorOut(id=new_id, **auth_in.model_dump())
    auths.append(auth.model_dump())
    return auth

def get_author_by_id(auth_id: int):
    for author in auths:
        if author["id"] == auth_id:
            return author
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Author with {auth_id} not found.")

