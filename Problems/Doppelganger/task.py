hashes = [hash(item) for item in object_list if isinstance(item, collections.Hashable)]
indeces = [i for i, item in enumerate(hashes) if hashes.count(item) > 1]
print(len(indeces))