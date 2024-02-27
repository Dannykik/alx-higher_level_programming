# models/base.py

class Base:
    """Base class for managing id attribute."""
    
    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        """Initialize Base instance with id."""
        if id is not None:  # if id is provided
            self.id = id  # assign id
        else:
            type(self).__nb_objects += 1  # increment __nb_objects
            self.id = type(self).__nb_objects  # assign new id

if __name__ == "__main__":
    # Test cases
    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
