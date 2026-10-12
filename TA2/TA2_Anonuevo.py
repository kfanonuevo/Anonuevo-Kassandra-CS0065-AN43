import random

# ==========================================
# TA2 - RULE-BASED AGENT 
# Anonuevo, Kassandra - AN43
# INCLUDING BONUS TASK
# ==========================================

# -------- Set Up Environment --------

environment = {
    "A": input("Is room A Dirty or Clean? ").strip().capitalize(),
    "B": input("Is room B Dirty or Clean? ").strip().capitalize(),
    "C": input("Is room C Dirty or Clean? ").strip().capitalize()
}

steps = int(input("\nHow many steps should the agent run? "))


# -------- Environment Functions --------

def is_dirty(room):
    return environment[room] == "Dirty"


def clean_room(room):
    environment[room] = "Clean"


# -------- Rule-Based Agent --------

class VacuumAgent:

    def __init__(self):
        self.location = "A"

    def move(self):
        rooms = list(environment.keys())

        # Move to a random room
        possible_rooms = [
            room for room in rooms
            if room != self.location
        ]

        self.location = random.choice(possible_rooms)

    def perceive_and_act(self):

        # Rule 1: Clean current room if dirty
        if is_dirty(self.location):
            clean_room(self.location)
            return f"Cleaned room {self.location}"

        # Bonus: Find dirty rooms
        dirty_rooms = [
            room for room in environment
            if is_dirty(room)
        ]

        # Bonus: Randomly choose a dirty room
        if dirty_rooms:
            self.location = random.choice(dirty_rooms)
            return f"Moving to room {self.location}"

        # If all rooms are clean
        return "All rooms are clean. Agent is idle."


# -------- Text-Based Grid --------

def show_grid(agent):

    grid = []

    for room in environment:

        if room == agent.location:
            grid.append(f"[{room}-Agent]")

        else:
            state = "Dirty" if is_dirty(room) else "Clean"
            grid.append(f"[{room}-{state}]")

    print("  ".join(grid))


# -------- Run Simulation --------

agent = VacuumAgent()

print("\nSimulation Starting...\n")

for step in range(1, steps + 1):

    print(f"Step {step}:")

    show_grid(agent)

    action = agent.perceive_and_act()

    print(action)

    show_grid(agent)

    print("Environment state:", environment)
    print()


print("Simulation finished.")