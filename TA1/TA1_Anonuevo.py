import agentpy as ap
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import Counter

# User input
num_agents = int(input("Enter number of agents: "))
grid_size = int(input("Enter grid size: "))
num_steps = int(input("Enter number of steps: "))


# Agent
class RandomWalker(ap.Agent):

    def setup(self):
        self.position = (
            random.randint(0, self.model.p.grid_size[0] - 1),
            random.randint(0, self.model.p.grid_size[1] - 1)
        )
        self.path = [self.position]

    def step(self):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Task 2: preferred right direction
        if self.model.p.preferred:
            directions = [(1, 0), (1, 0), (1, 0),
                          (-1, 0), (0, 1), (0, -1)]

        dx, dy = random.choice(directions)
        x, y = self.position

        x = max(0, min(self.model.p.grid_size[0] - 1, x + dx))
        y = max(0, min(self.model.p.grid_size[1] - 1, y + dy))

        self.position = (x, y)
        self.path.append(self.position)


# Model
class RandomWalkModel(ap.Model):

    def setup(self):
        self.agents = ap.AgentList(self, self.p.agents, RandomWalker)

    def step(self):
        for agent in self.agents:
            agent.step()


# Create model
def create_model(agents, size, steps, preferred=False):
    parameters = {
        "agents": agents,
        "grid_size": (size, size),
        "steps": steps,
        "preferred": preferred
    }

    model = RandomWalkModel(parameters)
    model.setup()
    return model


# Original animation
model = create_model(num_agents, grid_size, num_steps)

fig, ax = plt.subplots()
ax.set_xlim(0, grid_size)
ax.set_ylim(0, grid_size)
ax.set_xticks(range(grid_size + 1))
ax.set_yticks(range(grid_size + 1))
ax.grid(True)

scat = ax.scatter([], [], s=200)

def update(frame):
    if frame > 0:
        model.step()

    x = [a.position[0] for a in model.agents]
    y = [a.position[1] for a in model.agents]

    scat.set_offsets(list(zip(x, y)))
    ax.set_title(f"Random Walk - Step {frame}")

    return scat,

ani = animation.FuncAnimation(
    fig,
    update,
    frames=num_steps + 1,
    interval=500,
    repeat=False
)

plt.show()


# Task 1: Agent paths
plt.figure()

for i, agent in enumerate(model.agents):
    x, y = zip(*agent.path)
    plt.plot(x, y, marker=".", label=f"Agent {i + 1}")

plt.title("Task 1: Agent Paths")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

if num_agents <= 10:
    plt.legend()

plt.show()


# Task 2: Preferred direction
preferred = create_model(
    num_agents, grid_size, num_steps, preferred=True
)

for _ in range(num_steps):
    preferred.step()

plt.figure()

for i, agent in enumerate(preferred.agents):
    x, y = zip(*agent.path)
    plt.plot(x, y, marker=".", label=f"Agent {i + 1}")

plt.title("Task 2: Preferred Right Direction")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

if num_agents <= 10:
    plt.legend()

plt.show()


# Task 3: Final positions
print("\nTASK 3: FINAL POSITIONS")

positions = [a.position for a in model.agents]

for i, pos in enumerate(positions):
    print(f"Agent {i + 1}: {pos}")

print("Occupied cells:", len(Counter(positions)))

x, y = zip(*positions)

plt.figure()
plt.scatter(x, y, s=150)
plt.title("Task 3: Final Agent Positions")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()


# Task 4: Compare scenarios
scenario_a = create_model(5, 10, 20)
scenario_b = create_model(20, 10, 50)

for _ in range(20):
    scenario_a.step()

for _ in range(50):
    scenario_b.step()

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

for ax, scenario, title in zip(
    axes,
    [scenario_a, scenario_b],
    ["Scenario A", "Scenario B"]
):

    for agent in scenario.agents:
        x, y = zip(*agent.path)
        ax.plot(x, y, marker=".", markersize=3)

    ax.set_title(
        f"{title}: {scenario.p.agents} Agents, "
        f"{scenario.p.steps} Steps"
    )
    ax.grid(True)

plt.tight_layout()
plt.show()

print("\nAll tasks completed.")
