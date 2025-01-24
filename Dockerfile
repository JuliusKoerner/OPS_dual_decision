FROM pytorch/pytorch:2.4.1-cuda12.4-cudnn9-runtime


RUN apt update && apt install -y git python3-dev python3-pip
# RUN conda install python=3.8 -y
RUN pip install --no-cache-dir \
    cython \
    submitit \
    scipy \
    rich \
    opencv-python \
    numpy\
    shapely \
    pandas \
    wandb \
    seaborn \
    scikit-learn \
    Embeddings2Image \
    pycocotools \
    git+https://github.com/cocodataset/panopticapi.git#egg=panopticapi 




#RUN apt install -y python3-dev python3-pip
RUN python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y





