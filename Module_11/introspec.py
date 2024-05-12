import inspect


class Introspector:
    def __init__(self, obj):
        self.obj = obj

    def get_type(self):
        return type(self.obj).__name__

    def get_attributes(self):
        # аналогичная запись
        # attrs = []
        # for attr in dir(self.obj):
        #     if not inspect.ismethod(getattr(self.obj, attr)):
        #         attrs.append(attr)
        # return attrs
        return [attr for attr in dir(self.obj) if not inspect.ismethod(getattr(self.obj, attr))]

    def get_methods(self):
        # аналогичная запись
        # methods = []
        # for method in dir(self.obj):
        #     if inspect.ismethod(getattr(self.obj, method)):
        #         methods.append(method)
        # return methods
        return [method for method in dir(self.obj) if inspect.ismethod(getattr(self.obj, method))]

    def get_module(self):
        module = inspect.getmodule(self.obj)
        return module.__name__ if module else None

    def introspection_info(self):
        info = {
            'type': self.get_type(),
            'attributes': self.get_attributes(),
            'methods': self.get_methods(),
            'module': self.get_module()
        }
        return info

    def __str__(self):
        info = self.introspection_info()
        result = f"Introspection Info for object - {self.obj}:\n"
        result += f"Type: {info['type']}\n"
        result += f"Attributes: {', '.join(info['attributes'])}\n"
        result += f"Methods: {', '.join(info['methods'])}\n"
        result += f"Module: {info['module']}\n"
        return result


if __name__ == '__main__':
    number_introspector = Introspector(42)
    print(number_introspector)
    print('-' * 50)

    print(Introspector(Introspector))
