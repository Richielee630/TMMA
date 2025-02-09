import torch
import time
from transformers import DistilBertTokenizer, DistilBertModel

# 加载模型和 tokenizer
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
model = DistilBertModel.from_pretrained("distilbert-base-uncased")

# 测试输入
# text = "The quick brown fox jumps over the lazy dog."
text = "I love deep learning. It's very interesting."
 
inputs = tokenizer(text, return_tensors="pt")  # 转换为 PyTorch tensor

# 统计数据
total_matmul_count = 0
total_parameters = sum(p.numel() for p in model.parameters())
start_time = time.time()

# 在 CPU 上执行
with torch.no_grad():
    outputs = model(**inputs)

end_time = time.time()
execution_time = end_time - start_time  # 计算总执行时间

# 统计矩阵乘法 (MatMul) 次数
for name, module in model.named_modules():
    if isinstance(module, torch.nn.Linear):  # 线性层执行 MatMul
        total_matmul_count += 1

# 获取最终隐藏状态
hidden_states = outputs.last_hidden_state
print("\n===== DistilBERT 计算统计 =====")
print(f"Hidden States Shape: {hidden_states.shape}")
print(f"Total Parameters: {total_parameters:,}")  # 参数量
print(f"Total MatMul Count: {total_matmul_count}")  # 矩阵乘法次数
print(f"Execution Time: {execution_time:.6f} sec")  # 运行时间