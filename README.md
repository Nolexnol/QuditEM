# QUDIT_EM: Generalized PCS for qudit error mitigation

## Dependencies
This project uses **cirq** for circuit implementations and **seaborn** for data visualization.

## Installation
You can install these dependencies using pip:

```bash
pip install cirq seaborn
```

## Notes on current simulation assumptions
- The default qudit noise primitive is a **single-qudit depolarizing channel** (`QuditDepolarizingChannel`) parameterized by probability `p`.
- In the GHZ experiment notebook, noisy and ideal circuits are compared with Hellinger fidelity, and PCS uses ancilla postselection.
- Interpretations of dimension scaling should be made alongside circuit depth and postselection acceptance-rate trends.
