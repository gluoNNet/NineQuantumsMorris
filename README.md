# NineQuantumsMorris
This repository includes the code developed during the CERN Webfest 2019. 
A D-Wave Quantum Annealer is used to find the minimum of a Hamiltonian that is formed using the setup of a 9 men's morris board. Currently this Hamiltonian is based on our logic, but it might be subject of a machine learning algortihm. 

### TODO
- [ ] Update the models for better readability and better Hamiltonian calculation
- [ ] Update gui.py for more readability 
- [ ] Add explanation of Ising model and creation of Hamiltonian

### Model files

* 9qmorris.py : Basic model of the 9 quantum model
* 9qmorris_defensive.py : Defensive Hamiltonian construction
* 9qmorris_agressive.py : Agressive Hamiltonian construction
* 9qmorris_graph.py : Plots graphs used for the DWAVE annealer

### BOARDS
Files in boards-folder includes boards for 3 and 9 men's morris.
* board.py: Board for 3 men's morris
* board24.py: Board for 9 men's morris

### GUI

* pictures: folder that contains graphics elements for GUI
* gui.py: contains gui (taken from another github)
