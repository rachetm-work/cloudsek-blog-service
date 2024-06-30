import uvicorn
from fastapi import FastAPI

from src.framework.routers.blog import router as blog_router
from src.framework.settings.settings import settings

app = FastAPI()

app.include_router(router=blog_router, prefix=settings.base_url_prefix, tags=["blog"])

# For local debugging purposes only
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
