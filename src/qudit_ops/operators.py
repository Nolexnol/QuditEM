import cirq
import numpy as np
from typing import Tuple

#TODO: Generalize to qudits of any dimension

# Core 4th root of unity
gamma = np.exp(1j * 2 * np.pi / 4)  # = i


class ZGate(cirq.Gate):
    #Applies a generalized Z gate to a ququart.
    def __init__(self, power: int):
        self.power = power

    def _qid_shape_(self):
        return (4,)

    def _unitary_(self):
        return np.array([[1, 0, 0, 0],
                        [0, gamma**(self.power), 0, 0],
                        [0, 0, gamma**(2*(self.power)), 0],
                        [0, 0, 0, gamma**(3*(self.power))]])

    def _circuit_diagram_info_(self, args):
        return 'Z'+str(self.power) if self.power != 1 else 'Z'


class QuquartPlusGate(cirq.Gate):
    #Applies a modulo add to a ququart.
    def _qid_shape_(self):
        return (4,)

    def _unitary_(self):
        return np.array([[0, 0, 0, 1],
                         [1, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 0, 1, 0]])

    def _circuit_diagram_info_(self, args):
        return '[+]'


class QuquartPlusSquaredGate(cirq.Gate):
    #Applies a modulo add of 2 to a ququart.

    def _qid_shape_(self):
        return (4,)

    def _unitary_(self):
        return np.array([[0, 0, 1, 0],
                        [0, 0, 0, 1],
                        [1, 0, 0, 0],
                        [0, 1, 0, 0]])

    def _circuit_diagram_info_(self, args):
        return '[++]'


class QuquartPlusCubedGate(cirq.Gate):

    # Applies a modulo add gate cubed to a ququart.
    def _qid_shape_(self):
        return (4,)

    def _unitary_(self):
        return np.array([[0, 1, 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1],
                        [1, 0, 0, 0]])

    def _circuit_diagram_info_(self, args):
        return '[+++]'
    
    import cirq
import numpy as np
from typing import Tuple


class FlipGate(cirq.Gate):
    """
    Generalized flip gate that maps basis state |i⟩ to |j⟩ in a qudit of dimension d.
    
    """
    def __init__(self, d: int, i: int, j: int):
        try:
            0 <= i < d and 0 <= j < d
        except AssertionError:
            raise ValueError("i and j must be valid basis states for given dimension d")
        self.d = d
        self.i = i
        self.j = j

    def _qid_shape_(self):
        return (self.d,)

    def _unitary_(self):
        X_flip = np.eye(self.d, dtype=complex)
        X_flip[[self.i, self.j]] = X_flip[[self.j, self.i]]
        return X_flip

    def _circuit_diagram_info_(self, args):
        return f"X({self.i},{self.j})"

class ControlFlipGate(cirq.Gate):
    """
    Generalized controlled flip gate that maps basis state |i⟩ to |j⟩ in a qudit of dimension d,
    conditioned on a control qudit being in state |c⟩.
    """
    def __init__(self, d: int, c: int, i: int, j: int):
        self.d = d
        self.c = c
        self.i = i
        self.j = j

    def _qid_shape_(self):
        return (self.d, self.d)

    def _unitary_(self):
        X_flip = np.eye(self.d, dtype=complex)
        X_flip[[self.i, self.j]] = X_flip[[self.j, self.i]]
        return np.kron(X_flip, np.eye(self.d))

    def _circuit_diagram_info_(self, args):
        return f"CX({self.c}, {self.i}, {self.j})"
