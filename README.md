# 多模态情感分析

## 代码目录说明

```
├── 实验五数据   #　存放数据
|  └── data  #包含所有训练文本和图片，每个文件按照唯一的guid命名　　
|  └── train.txt #数据的guid和对应的情感标签　
|  └── test_without_label.txt #数据的guid和对应的情感标签，测试集
|  └── dev.tsv #经过处理后的验证集数据
|  └── train.tsv #经过处理后的训练集数据
|  └── test.tsv #经过处理后的测试集数据
├── metrics　　　　　　　　　# metrics计算
|  └── compute.py　　　
├── outputs              # 模型输出保存
|  └── pytorch_encoder.bin #保存的最好模型
|  └── pytorch_model.bin  #保存的最好模型
|  └── test_without_label.txt #最终预测结果
├── pre_trained_model　# 预训练模型
|  └── renet152.pth
├── processors　　　　　# 辅助函数
|  └── util.py
├── models　　　# 模型
|  └── model.py
|  └── resnet.py
├── get_data.py　#　数据处理
├── run.py       # 主程序
├── run.sh   #　任务运行脚本
├── run_image_only.sh   #　任务运行脚本
├── run_text_only.sh   #　任务运行脚本
├── run_test.sh   #　任务运行脚本
```

### 
## Requirements
```
pip install -r requirements.txt
```


## 运行

1. 通过该链接(https://download.pytorch.org/models/resnet152-b121ed2d.pth)下载预训练模型ResNet-152，并将该模型放入pre_trained_model文件下

2. 进行数据处理:

```
./get_data.py
```

**注意**: 该步骤可以省略，实验五数据下已经包含处理完成的数据了

3. 直接运行对应任务sh脚本，如：

```
sh run.sh #文本+图像
```
```
sh run_text_only.sh #仅文本
```
```
sh run_image_only.sh #仅图像
```

### 
## 参考

- https://github.com/huggingface/transformers.
- https://github.com/jefferyYu/TomBERT
- https://github.com/pytorch/vision/blob/main/torchvision/models/resnet.py
- https://github.com/ChineseGLUE/ChineseGLUE/tree/master/baselines/models_pytorch/classifier_pytorch