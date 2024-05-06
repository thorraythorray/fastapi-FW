from typing import Union
from fastapi import HTTPException, FastAPI
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse


class RequestError(HTTPException):
    def __init__(self) -> None:
        status_code = status.HTTP_400_BAD_REQUEST
        detail = 'Bad request'
        super().__init__(status_code, detail)


class ServerError(HTTPException):
    def __init__(self) -> None:
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        detail = 'Internal Server Error'
        super().__init__(status_code, detail)


class NotFound(HTTPException):
    def __init__(self) -> None:
        status_code = status.HTTP_404_NOT_FOUND
        detail = 'Not found'
        super().__init__(status_code, detail)


# 更改系统内置的异常处理，例如统一处理500的response为TemplateResponse
# app.add_exception_handler(HTTP_500_INTERNAL_SERVER_ERROR, server_error_exception)


# 自定义异常
class AppServiceError(Exception):
    def __init__(self, message: Union[str, None] = None):
        self.message = message if message else 'App Service Error'


# 处理自定义异常
async def register_exception_handlers(app: FastAPI):

    @app.exception_handler(AppServiceError)
    async def _(request: Request, exc: AppServiceError):
        return JSONResponse(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=exc.message
        )