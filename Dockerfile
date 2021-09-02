FROM pytorch/pytorch:1.8.1-cuda10.2-cudnn7-runtime

RUN apt update -qq -y && apt install -qq -y git && pip install gdown torchsummary matplotlib pandas sklearn tqdm tensorboard google-cloud-storage  && rm -rf /var/lib/apt/lists/*