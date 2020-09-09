"""Example Tasks for PyInvoke
"""


# pylint: disable=import-error
from invoke import task
# pylint: enable=import-error


@task
def hello_world(ctx):
    """Hello, World! task
    """
    ctx.run(' '.join(('echo',
                      'Hello,',
                      'World!')))
