# Brownian Motion Simulation
  
This code simulates Brownian motion, a random movement of particles suspended in a fluid (e.g., gas or liquid), and visualizes the resulting trajectory of a single particle using a matplotlib animation.

## Code Breakdown:

1. Import necessary libraries:
   - `numpy`: for numerical operations.
   - `matplotlib.pyplot`: for plotting.
   - `matplotlib.animation`: for creating animations.

2. Define the `BrownianMotion` class, which contains methods for simulating and plotting Brownian motion.

### BrownianMotion class

The `BrownianMotion` class has the following methods:

- `__init__(self, arena_size, num_steps)`: Initializes the Brownian motion simulation.
  - `arena_size`: The size of the square arena in which the particle moves.
  - `num_steps`: The number of time steps for the simulation.
  - `position`: The current position of the particle (initially set to the center of the arena).
  - `direction`: The current direction of the particle (initially set to a random value between 0 and 2 * pi).
  - `positions`: A list of the particle's positions over time (initially containing the initial position).

- `step(self)`: Updates the particle's position based on its current direction. If the particle hits the arena's boundary, it chooses a new random direction and ensures the position remains within the arena's limits.

- `simulate(self)`: Runs the Brownian motion simulation for the specified number of steps by calling `step()` repeatedly.

- `plot(self)`: Plots the particle's trajectory using a matplotlib animation.
  - `init()`: Initializes the animation by setting an empty data array for the line plot.
  - `animate(i)`: Updates the line plot with the particle's positions up to the current frame `i`.
  - `FuncAnimation()`: Creates an animation by repeatedly calling `animate()` for each frame of the simulation.

### Main code execution

- Set the `arena_size` and `num_steps` parameters.
- Create a `BrownianMotion` object.
- Run the simulation using the `simulate()` method.
- Plot the resulting trajectory using the `plot()` method.
