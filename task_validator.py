from abc import ABCMeta, abstractmethod

class Validator(metaclass=ABCMeta):

        @abstractmethod
        def validate(self):
            pass

        types = {}

        @classmethod
        def add_types(cls):
            return cls.types

        @classmethod
        def add_type(cls, name, klass):
            if not name:
                raise ValidatorException('Validator must have a name!')
            if not issubclass(klass, Validator):
                raise ValidatorException (
                    'Class {} is not validator'.format(klass)
                )
            cls.types[name] = klass

        @classmethod
        def get_instance(cls, name):

            klass = cls.types.get(name)
            if klass is None:
                raise ValidatorException(
                    'Validator {} не найден'.format(name)
                )
            return klass()


class EMailValidator(Validator):

    def validate(self, value):
        if value.count('@') > 1 or value.count('@') == 0:
            return False

        [name,domain] = value.split('@')
        if domain.count('.') == 0:
            return False

        return True

# class DateTimeValidator(object):
#     pass



Validator.add_type('email', EMailValidator)


if __name__ == '__main__':
    validator = Validator.get_instance('email')
    print(validator.validate('info@itmo-it.org'))
    print(validator.validate('infoitmo-it.org'))
    print(validator.validate('info@@itmo-it.org'))
    print(validator.validate('info@itmo-itorg'))
