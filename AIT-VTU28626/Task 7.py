# Operators
def move(subject, x1, x2):
    return f"Move {subject} from {x1} to {x2}"

def push_box(x1, x2):
    return f"Push box from {x1} to {x2}"

def climb_box(x, direction):
    return f"Climb box at {x} {direction}"

def have_banana(x):
    return f"Have banana at {x}"


# Initial State
initial_state = {
    'monkeyAt': 0,
    'monkeyLevel': 'Down',
    'bananaAt': 1,
    'boxAt': 2
}

# Goal State
goal_state = {
    'GetBanana': True
}


# Planning Algorithm
def plan_actions(initial_state, goal_state):
    actions = []

    monkey = initial_state['monkeyAt']
    box = initial_state['boxAt']
    banana = initial_state['bananaAt']

    # Step 1: Move monkey to box
    if monkey != box:
        actions.append(move("Monkey", monkey, box))
        monkey = box

    # Step 2: Push box to banana
    if box != banana:
        actions.append(push_box(box, banana))
        box = banana
        monkey = banana

    # Step 3: Climb box
    actions.append(climb_box(banana, "Up"))

    # Step 4: Take banana
    actions.append(have_banana(banana))

    return actions


# Execute
actions = plan_actions(initial_state, goal_state)

print("Plan:")
for action in actions:
    print(action)
