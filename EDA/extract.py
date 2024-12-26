import json

def count_contrast_phases(json_file):
    # Load JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Initialize dictionary to store cases by contrast phase
    contrast_phases = {}
    
    # Iterate through each case
    for case_id, case_info in data.items():
        phase = case_info['contrast_phase']
            
        # Add case ID to appropriate phase list
        if phase not in contrast_phases:
            contrast_phases[phase] = []
        contrast_phases[phase].append(case_id)
    
    # Print results
    print("Distribution of cases by contrast phase:")
    print("-" * 40)
    for phase, cases in sorted(contrast_phases.items()):
        print(f"{phase}:")
        print(f"Count: {len(cases)}")
        print(f"Case numbers: {', '.join(cases)}")
        print("-" * 40)
    
    # Store results in JSON file
    output_data = {
        phase: {
            "count": len(cases),
            "case_numbers": cases
        }
        for phase, cases in contrast_phases.items()
    }
    
    with open('contrast_phases_distribution.json', 'w') as f:
        json.dump(output_data, f, indent=4)
    
    print("\nResults have been saved to 'contrast_phases_distribution.json'")
    
    return contrast_phases

# Run the function
contrast_phases = count_contrast_phases('patient_info_train.json')