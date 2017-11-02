from abc import ABCMeta, abstractmethod
import datetime

class ValidatorException(Exception):
    pass

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
                    'Validator with name "{}" not found'.format(name)
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


class DateTimeValidator(Validator):

    def validate(self, value):
        valid_date = [
            '%Y-%m-%d',
            '%Y-%m-%d %H:%M',
            '%Y-%m-%d %H:%M:%S',
            '%d.%m.%Y',
            '%d.%m.%Y %H:%M',
            '%d.%m.%Y %H:%M:%S',
            '%d/%m/%Y',
            '%d/%m/%Y %H:%M',
            '%d/%m/%Y %H:%M:%S',
        ]

        for forms in valid_date:
            try:
                datetime.datetime.strptime(value, forms)
                return True
            except ValueError:
                continue
        return False



Validator.add_type('email', EMailValidator)
Validator.add_type('datetime', DateTimeValidator)

if __name__ == '__main__':
    validator = Validator.get_instance('email')
    print(validator.validate('info@itmo-it.org'))
    print(validator.validate('infoitmo-it.org'))
    print(validator.validate('info@@itmo-it.org'))
    print(validator.validate('info@itmo-itorg'))


    validator = Validator.get_instance('datetime')
    print(validator.validate('1.9.2017'))
    print(validator.validate('01/09/2017 12:00'))
    print(validator.validate('2017-09-01 12:00:00'))
