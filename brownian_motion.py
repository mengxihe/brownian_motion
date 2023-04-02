import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class BrownianMotion:

    def __init__(self, arena_size, num_steps):
        self.arena_size = arena_size
        self.num_steps = num_steps
        self.position = np.array([arena_size / 2, arena_size / 2])
        self.direction = np.random.rand() * 2 * np.pi
        self.positions = [self.position.copy()]

    def step(self):
        self.position += np.array([np.cos(self.direction), np.sin(self.direction)])

        for i in range(2):
            if self.position[i] < 0 or self.position[i] > self.arena_size:
                self.direction = np.random.rand() * 2 * np.pi
                self.position[i] = np.clip(self.position[i], 0, self.arena_size)

        self.positions.append(self.position.copy())

    def simulate(self):
        for _ in range(self.num_steps):
            self.step()

    def plot(self):
        fig, ax = plt.subplots()
        ax.set_xlim(0, self.arena_size)
        ax.set_ylim(0, self.arena_size)
        line, = ax.plot([], [], lw=2)

        def init():
            line.set_data([], [])
            return line,

        def animate(i):
            x = [pos[0] for pos in self.positions[:i+1]]
            y = [pos[1] for pos in self.positions[:i+1]]
            line.set_data(x, y)
            return line,

        ani = animation.FuncAnimation(fig, animate, frames=self.num_steps+1, init_func=init, interval=100, blit=True)

        plt.show()

if __name__ == "__main__":
    arena_size = 10
    num_steps = 200

    bm = BrownianMotion(arena_size, num_steps)
    bm.simulate()
    bm.plot()
