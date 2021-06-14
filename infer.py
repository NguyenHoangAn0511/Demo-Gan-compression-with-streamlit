import pickle
import time
import tqdm
import numpy as np
import torch
import torch
from models import create_model
from PIL import Image
import torchvision.transforms as transforms
import os
from utils.util import save_image, tensor2im
import streamlit as st
with open('opts/opt_full.pkl', 'rb') as f:
    opt = pickle.load(f)
model_full = create_model(opt, verbose=False)
model_full.setup(opt, verbose=False)


with open('opts/opt_compressed.pkl', 'rb') as f:
    opt = pickle.load(f)
model_ours = create_model(opt, verbose=False)
model_ours.setup(opt, verbose=False)


transform_list = [transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]
transform = transforms.Compose(transform_list)
imgs_dir = 'image'


def infer(imgs_dir):
    files = os.listdir(imgs_dir)
    file = files[0]
    if not file.endswith('.png'):
        return
    base = file.split('.')[0]
    path = os.path.join(imgs_dir, file)
    print(path)
    A_img = Image.open(path).convert('RGB')
    input = transform(A_img).to('cuda:0')
    input = input.reshape([1, 3, 256, 256])
    output_full = model_full.netG(input).cpu()
    output_ours = model_ours.netG(input).cpu()
    B_full = tensor2im(output_full)
    B_ours = tensor2im(output_ours)
    save_image(B_full, 'output/full/%s.png' % base, create_dir=True)
    save_image(B_ours, 'output/ours/%s.png' % base, create_dir=True)


def main():
    HomeScreen()

def HomeScreen():
    st.title("Horse to zibra translation")
    st.text("")
    st.text("")
    st.text("")
    c1, c2 = st.beta_columns([1,1])
    
    with c1:
        # st.header('Horse')
        video_file1 = open('data/output.mp4', 'rb')
        video_bytes1 = video_file1.read()
        st.video(video_bytes1, format='video/mp4', start_time=0)

    with c2:
        # st.header('Zebra')
        video_file = open('data/output_2.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes, format='video/mp4', start_time=0)
    
    
    _col1, _col2 = st.beta_columns([3,1])
    
    
    with _col1:
        UPLOADED_IMAGE = st.file_uploader(
            label='', type=['jpg', 'png', 'jpeg'])
        showfile = st.empty()
        if not UPLOADED_IMAGE:
            showfile.info('Please upload image file')
    
    with _col2:
        if UPLOADED_IMAGE:
            IMAGE = Image.open(UPLOADED_IMAGE)
            IMAGE = IMAGE.resize((256, 256))
            IMAGE = IMAGE.convert('RGB')
            IMAGE.save('image/USE_THIS.png')
            st.image(IMAGE, use_column_width=True)
    col1, col2 = st.beta_columns([1,1])
    
    # with col1:
        
    infer(imgs_dir)
    with col1:
        if UPLOADED_IMAGE:
            st.header('Compressed')
            IMAGE = Image.open('output/ours/USE_THIS.png')
            IMAGE = IMAGE.convert('RGB')
            IMAGE.save('image/USE_THIS.png')
            st.image(IMAGE, use_column_width=True)

    with col2:
        if UPLOADED_IMAGE:
            st.header('Full CycleGan')
            IMAGE = Image.open('output/full/USE_THIS.png')
            IMAGE = IMAGE.convert('RGB')
            IMAGE.save('image/USE_THIS.png')
            st.image(IMAGE, use_column_width=True)

if __name__ == '__main__':
    main()