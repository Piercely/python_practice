import torch
print(torch.__version__)  # 查看torch当前版本号
print(torch.version.cuda)  # 编译当前版本的torch使用的cuda版本号
print(torch.cuda.is_available())  # 查看当前cuda是否可用于当前版本的Torch，如果输出True，则表示可用
# 检查GPU是否可用
if torch.cuda.is_available():
    print("GPU可用！")
else:
    print("GPU不可用，将使用CPU进行计算。")


