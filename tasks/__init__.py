"""PyInvoke Main Task File
Write extra tasks in their own file. Then use the PyInvoke Collection to make
them part of their own namespace so that tasks can be repeated, but possibly
not overlapping.
"""


from invoke import Collection
from . import example_tasks_01

# This allows us to namespace our files.
namespace = Collection()
namespace.add_collection(example_tasks_01, name='ex01')
