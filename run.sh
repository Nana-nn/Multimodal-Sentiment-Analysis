# !/usr/bin/env bash

# εΎε+ζε­
 PYTHONIOENCODING=utf-8 CUDA_LAUNCH_BLOCKING=1 python run.py --output_dir ./output/ --do_train 1 --do_eval 1 --num_train_epochs 10 --warmup_proportion 0 --do_test 0