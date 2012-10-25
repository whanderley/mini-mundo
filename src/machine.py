class MachineInRepair(Exception):
    
    def __init__(self, code):
        self._code = code
    
    def __str__(self):
        return 'Machine %i already in repair' %self._code


class MachineNotInRepair(Exception):
    
    def __init__(self, code):
        self._code = code
    
    def __str__(self):
        return 'Machine %i not in repair' %self._code


class Machine(object):

    available = []
    problematic_machines = []

    @classmethod
    def available_machines(cls):
        return '\n'.join([machine.__repr__() for machine in Machine.available])

    def __init__(self, code, producer, sewing_types):
        self._code = code
        self._producer = producer
        self._sewing_types = sewing_types
        self._repairing = False
        self._repairs = []
        Machine.available.append(self)

    def __repr__(self):
        return 'producer: %s sewing types: %s' %(self.producer, ', '.join(self.sewing_types))

    def repair(self, supervisor, initiate):
        if self._repairing:
            raise MachineInRepair(self._code)
        else:
            self._repairs.append({'supervisor': supervisor, 'initiate': initiate})
            self._repairing = True
            if len(self._repairs) > 10:
                Machine.problematic_machines.append(self)
            Machine.available.remove(self)

    def finish_repair(self, end):
        if not(self._repairing):
            raise MachineNotInRepair(self._code)
        else:
            self._repairs[-1]['end'] = end
            self._repairing = False
            Machine.available.append(self)      
            
    def __getattr__(self, attr):
        if '_' + attr in self.__dict__:
            return getattr(self, '_' + attr)
        raise NameError

    def __setattr__(self, attr, value):
        if '_' + attr in self.__dict__:
            self.__dict__['_' + attr] = value
        else:
            self.__dict__[attr] = value