#!/bin/bash
#Experimental, does not work yet!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#newest cuda
# Environment name
ENV_NAME="eopsn_script"

# Ensure conda is available
if ! command -v conda &> /dev/null; then
    echo "Conda not found! Please install Miniconda or Anaconda first."
    exit 1
fi

echo "Creating Conda environment: $ENV_NAME"

# Create a new conda environment with Python 
conda create -y -n $ENV_NAME python=3.10

# Activate the environment
source $(conda info --base)/etc/profile.d/conda.sh
conda activate $ENV_NAME

export TORCH_CUDA_ARCH_LIST="9.0"



echo "Installing PyTorch with CUDA  support using pip..."
pip install torch==2.* torchvision torchaudio --index-url https://download.pytorch.org/whl/cu119

conda install -c nvidia cudatoolkit cudnn
conda install -c conda-forge cudatoolkit-dev #conda install -c nvidia -c conda-forge cuda-toolkit to install newer versions of the development kit


pip install cython submitit scipy rich shapely pandas wandb seaborn scikit-learn Embeddings2Image 
pip install pycocotools \
    git+https://github.com/cocodataset/panopticapi.git#egg=panopticapi

echo "install g++ for building detectron2"
conda install -c conda-forge gcc=10 gxx=10
cd detectron2
pip install -e .


