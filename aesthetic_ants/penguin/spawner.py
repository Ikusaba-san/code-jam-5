class Spawner:
    """Base class for spawning new game objects"""

    # This hack is just here so that this class doesn't need an __init__ method
    # because that can interfere with classes attempting to inherit from this
    # along with other bases.
    _created_objects = ()

    def __check_created_objects(self):
        if type(self._created_objects) is tuple:
            self._created_objects = []

    def create_object(self, cls: type, *args, **kwargs):
        """Creates an object and adds it to the list of pending objects.

        Parameters
        ----------
        cls:
            The class of the object you want to create
        args, kwargs:
            Any arguments to pass to cls

        """
        self.__check_created_objects()

        obj = cls(*args, **kwargs)
        self._created_objects.append(obj)
        return obj

    def created_objects(self) -> list:
        """Returns all the objects that were created since the last time\
        this was called.

        This clears the underlying list.
        """
        self.__check_created_objects()

        objects = self._created_objects.copy()
        self._created_objects.clear()
        return objects
