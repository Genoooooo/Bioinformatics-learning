import pandas as pd

# 加载数据
data = pd.read_csv("C:/BioProject/LiverCancer/simulated_liver_cancer.csv", index_col=0)

# 基础验证
print("=== 数据维度验证 ===")
print(f"基因数：{data.shape[0]}，样本数：{data.shape[1]}")  # 应为20000基因 x 100样本

print("\n=== 前5个基因示例 ===")
print(data.index[:5].tolist())  # 应显示基因ID如"ENSG00000000001"

print("\n=== 前3个样本表达值示例 ===")
print(data.iloc[:3, :3])