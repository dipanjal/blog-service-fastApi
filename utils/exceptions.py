from fastapi import HTTPException, status


def not_found(message: str = "content not found"):
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)


def not_allowed(message: str = "you are not permitted to perform this operation"):
    return HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail=message)
