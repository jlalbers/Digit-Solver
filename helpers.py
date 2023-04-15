class Solver:
    def __init__(self, target: int, numbers: list) -> None:
        self.target: int = target
        self.numbers: list = numbers
        self.solved: bool = False

    def solve(self):
        solution_moves: list = self.solve_helper(list(self.numbers), list())
        for move in solution_moves:
            print(f'{solution_moves.index(move) + 1}. {move}')
        self.solved = False

    def solve_helper(self, running: list, moves: list) -> list:
        # print(f'{(len(self.numbers) - len(running) + 1) * "    " + "|-"} Running: {running}')

        if len(running) == 1:
            return ['No solution']
        
        for i in range(len(running)):
            for j in range(len(running)):
                if i != j:

                    add_total, add_running, add_moves = \
                        self.add(i, j, list(running), list(moves))
                    if add_total == self.target:
                        self.solved = True
                        return add_moves
                    else:
                        new_moves = self.solve_helper(list(add_running), list(add_moves))
                        if self.solved:
                            return new_moves    
                    sub_total, sub_running, sub_moves = \
                        self.subtract(i, j, list(running), list(moves))
                    if sub_total == self.target:
                        self.solved = True
                        return sub_moves
                    elif sub_total >= 0:
                        new_moves = self.solve_helper(list(sub_running), list(sub_moves))
                        if self.solved:
                            return new_moves
                        
                    mul_total, mul_running, mul_moves = \
                        self.multiply(i, j, list(running), list(moves))
                    if mul_total == self.target:
                        self.solved = True
                        return mul_moves
                    else:
                        new_moves = self.solve_helper(list(mul_running), list(mul_moves))
                        if self.solved:
                            return new_moves
                    
                    if running[j] == 0 or isinstance(running[i] / running[j], float):
                        continue
                    div_total, div_running, div_moves = \
                        self.divide(i, j, list(running), list(moves))
                    if div_total == self.target:
                        self.solved = True
                        return div_moves
                    else:
                        new_moves = self.solve_helper(list(div_running), list(div_moves))
                        if self.solved:
                            return new_moves
                        
        return ['No solution']
                        

    def add(self, idx1: int, idx2: int, running: list, moves):
        # print(f'{(len(self.numbers) - len(running) + 1) * "    " + "|-"} Add {running[idx1]} and {running[idx2]}')
        new_total = running[idx1] + running[idx2]
        moves.append(f'{running[idx1]} + {running[idx2]} = {new_total}')
        running[idx1] = new_total
        running.pop(idx2)
        return new_total, running, moves
    
    def subtract(self, idx1: int, idx2: int, running: list, moves: list):
        # print(f'{(len(self.numbers) - len(running) + 1) * "    " + "|-"} Subtract {running[idx1]} and {running[idx2]}')
        new_total = running[idx1] - running[idx2]
        moves.append(f'{running[idx1]} - {running[idx2]} = {new_total}')
        running[idx1] = new_total
        running.pop(idx2)
        return new_total, running, moves

    def multiply(self, idx1: int, idx2: int, running: list, moves: list):
        # print(f'{(len(self.numbers) - len(running) + 1) * "    " + "|-"} Multiply {running[idx1]} and {running[idx2]}')
        new_total = running[idx1] * running[idx2]
        moves.append(f'{running[idx1]} x {running[idx2]} = {new_total}')
        running[idx1] = new_total
        running.pop(idx2)
        return new_total, running, moves
    
    def divide(self, idx1: int, idx2: int, running: list, moves: list):
        # print(f'{(len(self.numbers) - len(running) + 1) * "    " + "|-"} Divide {running[idx1]} and {running[idx2]}')
        new_total = running[idx1] // running[idx2]
        moves.append(f'{running[idx1]} / {running[idx2]} = {new_total}')
        running[idx1] = new_total
        running.pop(idx2)
        return new_total, running, moves
