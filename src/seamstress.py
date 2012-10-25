class Seamstress(object):

    def __init__(self, register, name, minimum_value, hability):
        self._register = register
        self._name = name
        if minimum_value < 0:
            raise ValueError
        else: 
            self._minimum_value = minimum_value 
        self._hability = hability


    def __getattr__(self, attr):
        if '_' + attr in self.__dict__:
            return getattr(self, '_' + attr)
        raise NameError

    def __setattr__(self, attr, value):
        if '_' + attr in self.__dict__:
            self.__dict__['_' + attr] = value
        else:
            self.__dict__[attr] = value