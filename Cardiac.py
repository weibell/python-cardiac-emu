from typing import List, Callable, Optional


class Cardiac:
    input: List[str]
    output: List[str]
    memory: List[Optional[int]]
    accumulator: int
    program_counter: int

    def __init__(self, program):
        self.input = program
        self.output = []
        self.memory = [1] + [None] * 99
        self.accumulator = 0
        self.program_counter = 0

    def run(self) -> List[str]:
        try:
            while True:
                self.step()
        except HaltException:
            return self.output

    def step(self) -> None:
        instruction_register: int = self.memory[self.program_counter]
        self.program_counter += 1

        opcode_handlers = {
            0: self._INP, 1: self._CLA, 2: self._ADD, 3: self._TAC, 4: self._SFT,
            5: self._OUT, 6: self._STO, 7: self._SUB, 8: self._JMP, 9: self._HRS
        }
        opcode = instruction_register // 100
        operand = instruction_register % 100
        opcode_handler: Callable[[int], None] = opcode_handlers[opcode]
        opcode_handler(operand)

    def _INP(self, address: int) -> None:
        self.memory[address] = int(self.input.pop(0))

    def _CLA(self, address: int) -> None:
        self.accumulator = self.memory[address]

    def _ADD(self, address: int) -> None:
        self.accumulator += self.memory[address]

    def _TAC(self, address: int) -> None:
        if self.accumulator < 0:
            self.program_counter = address

    def _SFT(self, places: int) -> None:
        places_left = places // 10
        places_right = places % 10
        self.accumulator = self.accumulator * 10 ** places_left % 10000
        self.accumulator = self.accumulator // 10 ** places_right

    def _OUT(self, address: int) -> None:
        zero_padded = str(self.memory[address]).zfill(3)
        self.output.append(zero_padded)

    def _STO(self, address: int) -> None:
        self.memory[address] = self.accumulator

    def _SUB(self, address: int) -> None:
        self.accumulator -= self.memory[address]

    def _JMP(self, address: int) -> None:
        self.memory[99] = 800 + self.program_counter
        self.program_counter = address

    def _HRS(self, address: int) -> None:
        self.program_counter = address
        raise HaltException


class HaltException(Exception):
    pass
