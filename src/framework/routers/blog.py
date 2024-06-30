from fastapi import APIRouter

from src.models.blog import BlogEntry
from src.services.blog_service import submit_blog, search_blogs

router = APIRouter(prefix="/blog")


@router.post("/submit")
async def submit_blog_handler(entry: BlogEntry):
    return submit_blog(entry)


@router.get("/search")
async def search_blogs_handler(search_term):
    return search_blogs(search_term)
