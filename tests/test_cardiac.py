import unittest

from Cardiac import Cardiac, HaltException


class TestCardiac(unittest.TestCase):
    def test_init(self):
        cardiac = Cardiac()
        self.assertEqual([], cardiac.input)
        self.assertEqual([], cardiac.output)
        self.assertEqual([1] + [None] * 99, cardiac.memory)
        self.assertEqual(0, cardiac.accumulator)
        self.assertEqual(0, cardiac.program_counter)

    def test_run(self):
        cardiac = Cardiac()
        cardiac.load(['002', '003', '942'])
        cardiac.run()
        self.assertEqual([1, 2, 3, 942] + [None] * 96, cardiac.memory)
        self.assertEqual(42, cardiac.program_counter)

    def test_INP(self):
        cardiac = Cardiac()
        cardiac.load(['100'])
        cardiac._INP(42)
        self.assertEqual([1] + [None] * 41 + [100] + [None] * 57, cardiac.memory)

    def test_CLA(self):
        cardiac = Cardiac()
        cardiac._CLA(0)
        self.assertEqual(1, cardiac.accumulator)

        cardiac.memory[42] = 100
        cardiac._CLA(42)
        self.assertEqual(100, cardiac.accumulator)

    def test_ADD(self):
        cardiac = Cardiac()
        cardiac.memory[42] = 9998

        cardiac._ADD(42)
        self.assertEqual(9998, cardiac.accumulator)

        cardiac._ADD(0)
        self.assertEqual(9999, cardiac.accumulator)

        cardiac._ADD(0)
        self.assertEqual(0, cardiac.accumulator)

    def test_TAC(self):
        cardiac = Cardiac()
        cardiac._TAC(42)
        self.assertEqual(0, cardiac.program_counter)

        cardiac.accumulator = -1
        cardiac._TAC(42)
        self.assertEqual(42, cardiac.program_counter)

    def test_SFT(self):
        cardiac = Cardiac()
        cardiac.accumulator = 42

        cardiac._SFT(0)
        self.assertEqual(42, cardiac.accumulator)

        cardiac._SFT(20)
        self.assertEqual(4200, cardiac.accumulator)

        cardiac._SFT(13)
        self.assertEqual(2, cardiac.accumulator)

        cardiac._SFT(1)
        self.assertEqual(0, cardiac.accumulator)

    def test_OUT(self):
        cardiac = Cardiac()
        cardiac.memory[42] = 100
        cardiac._OUT(0)
        cardiac._OUT(42)
        self.assertEqual(['001', '100'], cardiac.output)

    def test_STO(self):
        cardiac = Cardiac()
        cardiac.accumulator = 100
        cardiac._STO(42)
        self.assertEqual([1] + [None] * 41 + [100] + [None] * 57, cardiac.memory)

    def test_SUB(self):
        cardiac = Cardiac()
        cardiac._SUB(0)
        self.assertEqual(-1, cardiac.accumulator)

    def test_JMP(self):
        cardiac = Cardiac()
        cardiac.load(['842'])
        cardiac.step()
        cardiac.step()
        self.assertEqual(42, cardiac.program_counter)
        self.assertEqual([1, 842] + [None] * 97 + [802], cardiac.memory)

    def test_HRS(self):
        cardiac = Cardiac()
        with(self.assertRaises(HaltException)):
            cardiac._HRS(42)
        self.assertEqual(42, cardiac.program_counter)