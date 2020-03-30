class Singleton:
    def __init__(self, custom_class):
        self.custom_class = custom_class
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.custom_class(*args, **kwargs)
        return self.instance


@Singleton
class Man:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


father1, father2 = Man("Dima"), Man("Alex")
print(father1, father2)
print(father2 is father1)
