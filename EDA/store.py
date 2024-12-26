import json

def process_fold_splits(data):
    processed_folds = []
    
    # Process each fold
    for fold_name in data:
        fold_data = data[fold_name]
        processed_fold = {
            "train": [],
            "val": []
        }
        
        # Process training data
        for category in fold_data["train"]:
            # Add all images from this category to train list
            for img in fold_data["train"][category]:
                processed_fold["train"].append(img)
        
        # Process validation data
        for category in fold_data["val"]:
            # Add all images from this category to val list
            for img in fold_data["val"][category]:
                processed_fold["val"].append(img)
        
        # Sort the lists based on the number after 'im'
        processed_fold["train"].sort(key=lambda x: int(x.replace('im', '')))
        processed_fold["val"].sort(key=lambda x: int(x.replace('im', '')))
        
        processed_folds.append(processed_fold)
    
    return processed_folds

# Read the JSON file
with open('fold_splits.json', 'r') as f:
    fold_splits = json.load(f)

# Process the data
processed_data = process_fold_splits(fold_splits)

# Write the processed data to a new JSON file
with open('processed_fold_splits.json', 'w') as f:
    json.dump(processed_data, f, indent=4)  # Fixed: Added file object 'f' as the second argument

# Print example of first fold
print("First fold structure:")
print(json.dumps(processed_data[0], indent=4))