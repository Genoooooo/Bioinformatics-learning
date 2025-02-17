import pandas as pd
import numpy as np

# 设置随机种子（确保结果可复现）
np.random.seed(42)

# 生成基因ID（20000个）
genes = [f"ENSG{i:011d}" for i in range(1, 20001)]

# 生成样本ID（100个）
samples = [f"Sample{i:03d}" for i in range(1, 101)]

# 生成表达矩阵（20000基因 x 100样本）
data = pd.DataFrame(
    np.random.lognormal(mean=5, sigma=1, size=(20000, 100)),
    index=genes,
    columns=samples
)

import pandas as pd
import os

# 指定要保存的文件路径
file_path = "C:/BioProject/LiverCancer/simulated_liver_cancer.csv"

# 获取文件所在的目录
directory = os.path.dirname(file_path)

# 检查目录是否存在，如果不存在则创建
if not os.path.exists(directory):
    os.makedirs(directory)

# 保存数据到 CSV 文件
data.to_csv(file_path)

print("文件保存成功！")

# 保存数据
data.to_csv("C:/BioProject/LiverCancer/simulated_liver_cancer.csv")