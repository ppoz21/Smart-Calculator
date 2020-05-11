# create your dictionary here
from collections.abc import Hashable
objects_dict = {}
for object_ in objects:
    if isinstance(object_, Hashable):
        objects_dict[object_] = hash(object_)
