import traceback

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from src.framework.responses import ApiErrorResponse


class ExceptionMiddleware(BaseHTTPMiddleware):
    """
    This middleware will catch any exception that is raised from anywhere in the app and send an appropriate formatted response
    """

    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            return ApiErrorResponse(error_message=str(e), traceback=traceback.format_exc(), status_code=500)
