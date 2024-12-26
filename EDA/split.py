import json
import random

def create_fold_splits(json_file):
    # Load JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Create dictionaries to store cases by contrast phase
    phase_cases = {
        'arterial': [],
        'delayed': [],
        'no contrast agent': [],  # NC in the table
        'portal': [],
        'unkown': []  # U in the table
    }
    
    # Sort cases into phases
    for case_id, case_info in data.items():
        # Remove 'im' prefix if it exists
        clean_id = case_id[2:] if case_id.startswith('im') else case_id
        phase = case_info['contrast_phase']
        phase_cases[phase].append(clean_id)
    
    # Target distributions for each fold (train/val split)
    target_dist = [
        # (A_train, D_train, NC_train, P_train, U_train, A_val, D_val, NC_val, P_val, U_val)
        (26, 6, 2, 8, 6, 7, 2, 0, 2, 1),  # Fold 1
        (26, 7, 1, 8, 6, 7, 1, 1, 2, 1),  # Fold 2
        (26, 6, 2, 8, 6, 7, 2, 0, 2, 1),  # Fold 3
        (27, 6, 2, 8, 5, 6, 2, 0, 2, 2),  # Fold 4
        (27, 7, 1, 8, 5, 6, 1, 1, 2, 2)   # Fold 5
    ]
    
    # Initialize output dictionary
    folds = {}
    
    # Create each fold
    for fold_idx, dist in enumerate(target_dist, 1):
        train_set = {
            'arterial': [],
            'delayed': [],
            'no contrast agent': [],
            'portal': [],
            'unkown': []
        }
        val_set = {
            'arterial': [],
            'delayed': [],
            'no contrast agent': [],
            'portal': [],
            'unkown': []
        }
        
        # Create copies of phase_cases to work with
        available_cases = {phase: cases.copy() for phase, cases in phase_cases.items()}
        
        # Fill train set
        phases = ['arterial', 'delayed', 'no contrast agent', 'portal', 'unkown']
        train_counts = dist[:5]
        val_counts = dist[5:]
        
        for phase, count in zip(phases, train_counts):
            selected = random.sample(available_cases[phase], count)
            # Add 'im' prefix to each number
            train_set[phase].extend([f"im{case}" for case in selected])
            for case in selected:
                available_cases[phase].remove(case)
        
        # Fill validation set
        for phase, count in zip(phases, val_counts):
            selected = random.sample(available_cases[phase], count)
            # Add 'im' prefix to each number
            val_set[phase].extend([f"im{case}" for case in selected])
            for case in selected:
                available_cases[phase].remove(case)
        
        # Store in folds dictionary
        folds[f'fold_{fold_idx}'] = {
            'train': train_set,
            'val': val_set
        }
    
    # Save to JSON file
    with open('fold_splits.json', 'w') as f:
        json.dump(folds, f, indent=4)
    
    print("Fold splits have been saved to 'fold_splits.json'")
    
    return folds

# Set random seed for reproducibility
random.seed(42)

# Run the function
fold_splits = create_fold_splits('patient_info_train.json')