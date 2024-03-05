#QuantumMorseCodeTeleportation

Quantum Teleportation with Simulated Noise in Cirq

This Python program demonstrates the concept of quantum teleportation using Google's Cirq quantum computing framework. Quantum teleportation is a fundamental protocol in quantum information theory that allows the state of a qubit to be transmitted from one location to another, without moving the physical qubit itself. This is achieved through quantum entanglement and classical communication.

In this specific implementation, we simulate the teleportation of a Morse code symbol, represented as a quantum state, between qubits in a quantum circuit. The program first encodes a Morse code symbol ('-' for dash and '.' for dot) into the state of a qubit. It then uses an entangled pair of qubits to teleport this state from one qubit to another.

To add a layer of realism and challenge, the program incorporates a simulated noise model. This introduces a depolarizing error to each gate operation, mimicking the imperfections present in real quantum hardware. After applying the teleportation protocol under noisy conditions, the program outputs the final state of the teleported qubit, demonstrating how the initial state has been transferred despite the presence of quantum noise.

The final section of the code calculates and prints the probabilities of each possible state of the system after the teleportation, providing insight into how the noise affects the process. This program serves as an educational tool to understand both the power and the challenges of quantum teleportation in the presence of realistic noise conditions.
