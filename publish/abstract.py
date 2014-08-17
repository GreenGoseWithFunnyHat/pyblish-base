
# Standard library
import abc


class Filter(object):
    __families__ = []
    __hosts__ = []
    __version__ = (0, 0, 0)

    def __str__(self):
        return type(self).__name__

    def __repr__(self):
        return u"%s.%s(%r)" % (__name__, type(self).__name__, self.__str__())

    def __init__(self, instance):
        self.instance = instance
        self.errors = list()

    @abc.abstractmethod
    def process(self, instance):
        pass


class Selector(object):

    @abc.abstractmethod
    def process(self, instance):
        pass


class Validator(Filter):

    @abc.abstractmethod
    def fix(self, instance):
        pass


class Extractor(Filter):
    pass


class Context(set):
    @property
    def errors(self):
        """Return errors occured in contained instances"""
        errors = list()
        for instance in self:
            errors.extend(instance.errors)
        return errors

    @property
    def has_errors(self):
        """Return True if Context contains errors, False otherwise"""
        for error in self.errors:
            return True
        return False


class Instance(set):
    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        """E.g. Instance('publish_model_SEL')"""
        return u"%s(%r)" % (type(self).__name__, self.__str__())

    def __str__(self):
        """E.g. 'publish_model_SEL'"""
        return str(self.name)

    def __init__(self, name):
        super(Instance, self).__init__()
        self.name = name
        self.config = dict()
        self.errors = list()
