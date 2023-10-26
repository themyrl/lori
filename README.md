# LORI: Long and Out of Range Interaction transformer module for 3D medical image segmentation
official repository
preprint comming soon

## 1. Installattion
```
conda create --name lori
conda activate lori
conda install pip

pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116

cd nnUNet
pip install -e .
cd ../lori_package
pip install -e .
```

## 2. Dataset

### BCV
- Download [BCV Dataset](https://www.synapse.org/#!Synapse:syn3193805/wiki/217789)
- Preprocess the BCV dataset according to the uploaded nnUNet package
- Training and Testing ID are in fine_package/lori/datasets/splits_final.pkl
- Task017

### WORD
- Download [WORD Dataset](https://github.com/HiLab-git/WORD)
- Preprocess the WORD dataset according to the uploaded nnUNet package
- Task140


## 3. Training & Evaluation
To train LORI from scratch on WORD: 

```
python lori_package/lori/run/run.py -network nnUNetTrainerV2_LORI_nnUNet -task 140 -outpath LORI_OUT -na
```


To evluate LORI from scratch on WORD: 

```
python lori_package/lori/run/run.py -network nnUNetTrainerV2_LORI_nnUNet -task 140 -outpath LORI_OUT -na -only_val
```





## 4. Citation
Comming soon

## 5. Acknowledgements

Part of codes are reused from [nnU-Net](https://github.com/MIC-DKFZ/nnUNet). Thanks to Fabian Isensee for the codes of nnU-Net.



## Contact
Loic THEMYR ([loic.themyr@lecnam.net](loic.themyr@lecnam.net))
