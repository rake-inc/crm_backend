from celery.task import Task
from crm.app import app


class BaseTask(Task):

    def declare_queue(self, queue_name=""):
        if queue_name:
            self.queue = queue_name

    def run(self, *args, **kwargs):
        print("{}".format(kwargs))
        super(BaseTask, self).run(*args, **kwargs)

    def apply_async(self, args=None, kwargs=None, task_id=None, producer=None,
                    link=None, link_error=None, shadow=None, **options):
        super(BaseTask, self).apply_async(args=None, kwargs=None, task_id=None, producer=None, link=None,
                                          link_error=None, shadow=None, **options)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print("ON FAILURE {} for task_id {} from request_id {}".format(exc, task_id, self.request.id))
        # from celery.contrib.rdb import set_trace
        # set_trace()
        super(BaseTask, self).on_failure(exc, task_id, args, kwargs, einfo)

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        print("ON SUCCESS {} for task_id {} from request_id {}".format())
        super(BaseTask, self).on_retry(exc, task_id, args, kwargs, einfo)

    def on_success(self, retval, task_id, *args, **kwargs):
        super(BaseTask, self).on_success(retval, task_id, *args, **kwargs)


@app.task(
    max_retries=3,
    soft_time_limit=5,
    base=BaseTask)
def set_appointment(**kwargs):
    from celery.contrib.rdb import set_trace
    set_trace()
    print(kwargs)


@app.task(
    max_retries=3,
    soft_time_limit=5,
    base=BaseTask)
def remind_and_notify(**kwargs):
    print(kwargs)


app.tasks.register(BaseTask)
