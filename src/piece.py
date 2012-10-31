class Piece(object):

    def __init__(self, modelo, descricao):
        self._modelo = modelo
        self._descricao = descricao

    def __getattr__(self, attr):
        if '_' + attr in self.__dict__:
            return getattr(self, '_' + attr)
        raise NameError

    def __setattr__(self, attr, value):
        if '_' + attr in self.__dict__:
            self.__dict__['_' + attr] = value
        else:
            self.__dict__[attr] = value