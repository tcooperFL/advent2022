# day 10
from dataclasses import dataclass
from itertools import repeat

@dataclass
class Cpu:
    x: int = 1
    cycle: int = 0

    def run(self, program, debug=None, trace=False):
        self.x = 1
        self.cycle = 0
        self.debug = debug

        # Run the program
        for statement in program:
            if trace:
                print(f"[{self.cycle}]: {statement}")
            self._execute(statement)
    
    def _execute(self, instruction):
        match instruction:
            case ['addx', s]:
                self._inc_cycle()
                self._inc_cycle()
                self.x += int(s)
            case ['noop']:
                self._inc_cycle()
            case _:
                print(f"Bad instruction ignored - {instruction}")
    
    def _inc_cycle(self):
        self.cycle += 1
        if self.debug:
            self.debug(self)

def load_program():
    with open('data/day10.txt', 'r') as f:
        return list(map(lambda x: x.split(), f.readlines()))

def part1():
    samples = []
    def sample(cpu):
        if cpu.cycle in {20, 60, 100, 140, 180, 220}:
            signal = cpu.cycle * cpu.x
            print(f"During {cpu.cycle}th cycle, x = {signal}")
            samples.append(signal)

    cpu = Cpu()
    program = load_program()
    
    # Run with the sampler
    cpu.run(program, debug=sample)
    
    print(f"Sum of samples = {sum(samples)}")


def part2():
    pixels = list(repeat('.', 240))

    def paint_pixel(cpu):
        position = cpu.cycle % 40
        if abs((cpu.x + 1) - position) < 2:
            pixels[cpu.cycle] = '#'

    cpu = Cpu()
    program = load_program()
    
    # Run with the sampler
    cpu.run(program, debug=paint_pixel)

    print("Image")
    for row in range(6):
        start = row * 40
        print(''.join(pixels[start:start+40]))


if __name__ == '__main__':
    part1()
    # 17940
    part2()
    # ZCBAJFJZ