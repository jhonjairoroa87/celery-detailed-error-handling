from proj.celery_app import app as celery_app
from celery.utils.log import get_task_logger

celery_logger = get_task_logger(__name__)


class CallbackTask(celery_app.Task):
    """Defines a task class that handle a callback when the task fails"""

    def on_failure(self, exc, task_id, args, kwargs, error_info):
        """
        Catch the error raised in the task and add detailed error into to the logs
        :param exc: The exception raised by the task.
        :param task_id: Unique id of the failed task.
        :param args: Original arguments for the task that failed.
        :param kwargs: Original keyword arguments for the task that failed.
        :param error_info: ExceptionInfo instance, containing the traceback.
        """
        # Detailed error logging
        celery_logger.error("A task execution failed")
        celery_logger.error("task exception %s", exc)
        celery_logger.error("task_id %s", task_id)
        celery_logger.error("task args %s", args)
        celery_logger.error("task kwargs %s", kwargs)
        celery_logger.error("task error_info %s", error_info)


