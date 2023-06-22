import json
import os

# Load the JSON configuration from file
with open('config.json', 'r') as f:
    config = json.load(f)

# Change the mutation name
mutation_file_names = ['complete', 'limited']

for mutation in mutation_file_names:
    config["mutation"]["name"] = mutation

    pretty_data = json.dumps(config, indent=4)
    # Save the updated config to a new file
    with open('config.json', 'w') as f:
        f.write(pretty_data)

    # Change the mutation probability from 0 to 1 in increments of 0.1
    for p in range(0, 11):

        mutation_probability = p/10

        if p == 0:
                mutation_probability = p
        if p == 10:
                mutation_probability = 1

        # Update the mutation probability in the config
        config["mutation"]["probability"] = mutation_probability
        pretty_data = json.dumps(config, indent=4)

        # Save the updated config to a new file
        with open('config.json', 'w') as f:
            f.write(pretty_data)

        # Run the main.py script with the updated config
        os.system('python main.py m') 
