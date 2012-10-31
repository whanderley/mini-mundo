#encoding:utf-8

import unittest
from should_dsl import should, should_not
from piece import Piece


class TestPiece(unittest.TestCase):

	def setUp(self):
		self.piece = Piece('camisa polo', 'camisa polo dois botões e meio')

	def test_piece_initialization(self):
		self.piece.modelo |should| equal_to('camisa polo')
		self.piece.descricao |should| equal_to('camisa polo dois botões e meio')