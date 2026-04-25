import time

from django.http import HttpRequest

from core.utils.user import User

from logs.logger import logger
from logs.models import Log

class LoggingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        start_time = time.time()
        user = request.user if hasattr(request, 'user') and request.user.is_authenticated else 'Anonymous'

        try:
            response = self.get_response(request)
        except Exception:
            logger.exception(
                f"Exception sur {request.method} {request.path} par "
                f"{user}"
            )
            raise

        duration = time.time() - start_time
        log_level = "INFO"

        if response.status_code >= 500:
            log_level = "ERROR"
        elif response.status_code >= 400:
            log_level = "WARNING"

        duration = time.time() - start_time
        logger.log(
            log_level,
            f"{request.method} {request.path} "
            f"status={response.status_code} "
            f"user={user} "
            f"duration={duration:.3f}s"
        )

        Log.objects.create(
            level=log_level,
            method=request.method,
            path=request.path,
            user=user if isinstance(user, User) else None,
        )

        return response
