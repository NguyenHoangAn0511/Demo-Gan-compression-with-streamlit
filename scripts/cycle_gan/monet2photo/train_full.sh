#!/usr/bin/env bash
python train.py --dataroot database/monet2photo \
  --model cycle_gan \
  --netG resnet_9blocks \
  --log_dir logs/cycle_gan/monet2photo/full \
  --real_stat_A_path real_stat/monet2photo_A.npz \
  --real_stat_B_path real_stat/monet2photo_B.npz
