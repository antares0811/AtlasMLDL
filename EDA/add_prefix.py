import json

def add_im_prefix(data):
    """
    Add 'im' prefix to all IDs in both train and val lists.
    
    Args:
        data (list): List of dictionaries containing train and val lists
        
    Returns:
        list: Modified data with 'im' prefixes added
    """
    modified_data = []
    
    for fold in data:
        modified_fold = {
            'train': [f"im{id_}" for id_ in fold['train']],
            'val': [f"im{id_}" for id_ in fold['val']]
        }
        modified_data.append(modified_fold)
    
    return modified_data

# Load the data
# Load the data from external file
input_file = 'splits_final.json' 
with open(input_file, 'r') as f:
    data = json.load(f)

# Add the prefixes
modified_data = add_im_prefix(data)

# Save the modified data
with open('modified_data.json', 'w') as f:
    json.dump(modified_data, f, indent=4)
