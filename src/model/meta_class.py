from abc import ABCMeta


class ClassMeta(ABCMeta):
    required_attributes = []

    def __call__(cls):
        obj = super(ClassMeta, cls).__call__()
        for attribute_name in obj.required_attributes:
            if not getattr(obj, attribute_name):
                raise ValueError(f'Required attribute ({attribute_name}) not set')
        return obj
