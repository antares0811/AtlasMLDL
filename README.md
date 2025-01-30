# The Fine-tuned Robust Scalable nn-Unet-based Framework on Liver ATLAS Challenge Dataset
by Thanh-Huy Nguyen et.al. (Universite de Bourgogne, France)

This guide outlines the steps for fine-tuning the STU-Net model using the ATLAS dataset and running inference for result calculation.

Link to download the dataset: https://drive.google.com/drive/folders/1fq-pQClwGVEk8aKxUvu_MZV3wa2VtVlK?usp=sharing
## 1. Prepare the nnUNet Folders and environment

First, adjust the `nnUNet-2.2/nnunetv2/paths.py` to point to the appropriate folders:

- **nnUNet_raw**: Folder containing data to be preprocessed
- **nnUNet_preprocessed**: Folder where preprocessed data will be stored
- **nnUNet_results**: Folder for saving the results
  
 Install environment on nnUNet-2.2
```bash
cd nnUNet-2.2
pip install .
```
Check the integrity of the Raw Dataset using
```bash
python nnunetv2/experiment_planning/verify_dataset_integrity.py
```

If want to preprocessed of **NEW RAW DATA**

```bash
python nnunetv2/experiment_planning/plan_and_preprocess_entrypoints.py -c [3d_fullres,3d_lowres,...] -d <DATASET_ID>
```
examples
```bash
python nnunetv2/experiment_planning/plan_and_preprocess_entrypoints.py -c 3d_fullres -d 003
```

## 2. Adjust `splits_final.json` for Fine-Tuning

If new dataset now ATLAS
- Replace the current `splits_final.json` in with the one in dataset for training.

## 3. Fine-Tuning

For fine-tuning the model for different folds `[0, 1, 2, 3, 4]`, run the following command:

```bash
python nnunetv2/run/run_finetuning_stunet.py <DatasetID> 3d_fullres <FOLD> -pretrained_weights <MODEL_PATH> -tr STUNetTrainer_base_ft
```

**<DatasetID>**: The ID for the dataset (e.g., 3).
**<FOLD>**: The fold number (e.g., 0, 1, 2, etc.).
**<MODEL_PATH>**: Path to the pretrained model.

examples
```bash
python nnunetv2/run/run_finetuning_stunet.py 3 3d_fullres 2  -pretrained_weights '/mnt/c/Users/Quang Khai/Downloads/ATLAS/STU-Net/pretrained_models/small_ep4k.model' -tr STUNetTrainer_small_ft
```
## 4. Ensemble
...
## 5. Inference
To perform inference and get the results, adjust the directories for the model checkpoint and the test set. Run the following command:

```bash
python nnunetv2/inference/examples.py
```
- Make sure to adjust the directory to the correct model checkpoint and fold.
- Update the test set and result directory accordingly.
## 6. Calculate Metrics
Go to the Dataset Origin folder (e.g Dataset003_Liver) to execute the metric calculation. Adjust the inference result directory and the label test directory.

Run the following command to calculate the metrics:
```bash
python metric_calculation/calculate_metrics.py
```

## 7. Acknowledgment
Code is prepared by Thanh-Huy Nguyen (Universite de Bourgogne, France)
