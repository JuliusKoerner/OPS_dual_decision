#!/bin/bash
#Works for small gpus on tum
#installs development cuda toolkit, might need to run the sh make.sh command in mask2former/modelling/pixel_decoder/ops (or similar), for mask2former or p2f to work

# Environment name
ENV_NAME="eopsn_gpu7"


echo "Creating Conda environment: $ENV_NAME"

# Create a new conda environment with Python 
conda create -y -n $ENV_NAME python=3.10

conda activate $ENV_NAME


conda install pytorch torchvision torchaudio pytorch-cuda=12.4 -c pytorch -c nvidia
conda install -c nvidia -c conda-forge cuda-toolkit



python -c "import torch; print(torch.cuda.is_available(), torch.version.cuda)"

pip install cython submitit scipy rich shapely pandas wandb seaborn scikit-learn Embeddings2Image 
pip install pycocotools \
    git+https://github.com/cocodataset/panopticapi.git#egg=panopticapi

cd detectron2
pip install -e .


