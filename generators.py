def lstrip(generator):
    for item in generator:
        if not item.isspace():
            yield item
            break
    yield from generator
