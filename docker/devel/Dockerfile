FROM pytorch/pytorch:1.8.1-cuda10.2-cudnn7-devel

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update -qq -y && apt install -qq -y git jq && \
     pip install gdown torchsummary matplotlib pandas sklearn tqdm tensorboard google-cloud-storage click requests tqdm pyspng ninja imageio-ffmpeg==0.4.3

