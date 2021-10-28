FROM pytorch/pytorch:1.8.1-cuda10.2-cudnn7-runtime

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update -qq -y && apt install -qq -y git && \
     pip install gdown torchsummary matplotlib pandas sklearn tqdm tensorboard google-cloud-storage click requests tqdm pyspng ninja imageio-ffmpeg==0.4.3  && \
     rm -rf /var/lib/apt/lists/*

