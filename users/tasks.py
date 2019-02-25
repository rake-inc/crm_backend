from celery import task


@task
def add(x, y):
    print ("{}{}".format("=" * 7, ">Task called"))
    return x + y
