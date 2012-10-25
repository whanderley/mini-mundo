import unittest
from should_dsl import should, should_not
from machine import Machine, MachineInRepair, MachineNotInRepair


class TestMachine(unittest.TestCase):

	def setUp(self):
		Machine.available = []
		self.machine = Machine(1, 'Janome', ['overlock', 'zig-zag', 'costura reta'])

	def test_startup_machine(self):
		self.machine.code |should| equal_to(1)
		self.machine.producer |should| equal_to('Janome')
		self.machine.sewing_types |should| equal_to(['overlock', 'zig-zag', 'costura reta'])
		self.machine.repairing |should| equal_to(False)
		self.machine.repairs |should| equal_to([])
		Machine.available |should| equal_to([self.machine])

	def test_repair_machine(self):
		self.machine.repair('supervisor', '16-10-2012')
		self.machine.repairing |should| equal_to(True)
		self.machine.repairs |should| equal_to([{'supervisor': 'supervisor', 'initiate': '16-10-2012'}])
		Machine.available |should_not| contain(self.machine)
	 	(self.machine.repair, 'supervisor2', '17-10-2012') |should| throw(MachineInRepair)

	def test_finish_repair_machine(self):
	 	self.machine.repair('supervisor', '16-10-2012')
	 	self.machine.finish_repair('17-10-2012')
	 	self.machine.repairs |should| equal_to([{'supervisor': 'supervisor', 'initiate': '16-10-2012', 'end': '17-10-2012'}])
	 	self.machine.repairing |should| equal_to(False)
	 	Machine.available |should| contain(self.machine)
		(self.machine.finish_repair, '17-10-2012') |should| throw(MachineNotInRepair)

	def test_problematic_machine(self):
		for i in range(11):
			self.machine.repair('supervisor', '16-10-2012')
			self.machine.finish_repair('17-10-2012')
		len(self.machine.repairs) |should| equal_to(11)
		Machine.problematic_machines |should| contain(self.machine)

	def test_machines_avaiable(self):
		Machine.available_machines() |should| equal_to('producer: Janome sewing types: overlock, zig-zag, costura reta')



