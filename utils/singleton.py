class Singleton(type):

    _instance = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instance[cls] = instance
        return cls._instance [cls]