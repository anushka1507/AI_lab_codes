import random

# Transition matrix
transition_matrix = {
    'Sunny': {'Sunny': 0.8, 'Cloudy': 0.1, 'Rainy': 0.1},
    'Cloudy': {'Sunny': 0.4, 'Cloudy': 0.4, 'Rainy': 0.2},
    'Rainy': {'Sunny': 0.2, 'Cloudy': 0.5, 'Rainy': 0.3}
}

# Starting probabilities for each state
starting_probabilities = {'Sunny': 0.3, 'Cloudy': 0.4, 'Rainy': 0.3}

# Function to generate a sequence of states
def generate_state_sequence(matrix, start_probs, num_states):
    states = list(matrix.keys())
    current_state = random.choices(states, weights=[start_probs[state] for state in states])[0]
    sequence = [current_state]

    for _ in range(num_states - 1):
        next_state = random.choices(states, weights=[matrix[current_state][state] for state in states])[0]
        sequence.append(next_state)
        current_state = next_state

    return sequence

# Generate a sequence of 10 states
sequence_of_states = generate_state_sequence(transition_matrix, starting_probabilities, 10)

# Print the sequence of states
print("Sequence of States Generated:")
print(sequence_of_states)
