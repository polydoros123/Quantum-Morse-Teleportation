import cirq
import numpy as np

# Define the three qubits.
qubits = cirq.LineQubit.range(3)

# Create the circuit.
circuit = cirq.Circuit()

# Prepare an entangled pair (qubits 1 and 2).
circuit.append([cirq.H(qubits[1]), cirq.CNOT(qubits[1], qubits[2])])  

# Assume we want to teleport a Morse code symbol.
# For a dot, do nothing (state |0⟩). For a dash, apply X gate (state |1⟩).
morse_symbol = '.'  # Change to '-' for a dash
if morse_symbol == '-':
    circuit.append(cirq.X(qubits[0]))

# Apply the teleportation protocol.
circuit.append([cirq.CNOT(qubits[0], qubits[1]), cirq.H(qubits[0])])
circuit.append(cirq.measure(qubits[0], qubits[1]))
circuit.append([cirq.CNOT(qubits[1], qubits[2]), cirq.CZ(qubits[0], qubits[2])])

# Add depolarizing noise to the circuit.
noise = cirq.depolarize(p=0.01)  # 1% error probability for each gate
noisy_circuit = circuit.with_noise(noise)

# Display the noisy circuit.
print("Noisy Circuit:")
print(noisy_circuit)

# Simulate the noisy circuit.
simulator = cirq.DensityMatrixSimulator()
result = simulator.simulate(noisy_circuit)

# Output the final density matrix.
print("\nFinal density matrix with noise:")
print(result.final_density_matrix)

# To get the probabilities of each basis state, you can take the diagonal elements of the density matrix.
state_probabilities = np.diag(result.final_density_matrix).real
print("\nProbabilities of each basis state:")
for i, prob in enumerate(state_probabilities):
    print(f"State |{i:03b}> has probability {prob:.6f}")



    

