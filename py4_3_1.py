import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import numpy as np
import matplotlib.pyplot as plt
def given_data():
    """生成 XOR 数据集"""
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]).astype(np.float32)
    y = np.array([0, 1, 1, 0]).astype(np.float32)
    return X, y
def create_dataloader(X, y, batch_size=1, shuffle=False):
    """将 NumPy 数据封装为 DataLoader"""
    X_tensor = torch.tensor(X)
    y_tensor = torch.tensor(y, dtype=torch.float32).reshape(-1, 1)
    dataset = TensorDataset(X_tensor, y_tensor)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)
    return dataloader
BATCH_SIZE = 1      # 每次送入网络的样本数，可改为 2 或 4 观察影响
SHUFFLE    = False  # 是否在每个 epoch 打乱数据顺序
# ----------------------------

X_train, y_train = given_data()
train_loader = create_dataloader(X_train, y_train,
                                 batch_size=BATCH_SIZE,
                                 shuffle=SHUFFLE)

print(f'样本数: {len(X_train)}, 特征维度: {X_train.shape[1]}')
print(f'X =\n{X_train}')
print(f'y = {y_train}')
class SimpleNN(nn.Module):
    def __init__(self, input_size=2, hidden_size=4, output_size=1):
        super(SimpleNN, self).__init__()
        self.fc1     = nn.Linear(input_size, hidden_size)
        self.relu    = nn.ReLU()       # 可换成 nn.Tanh() / nn.Sigmoid() / nn.LeakyReLU()
        self.fc2     = nn.Linear(hidden_size, output_size)
        # self.sigmoid = nn.Sigmoid()  # 如果使用 BCELoss，需要取消此行注释

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        # out = self.sigmoid(out)      # 与上面 sigmoid 配套使用
        return out


# ---------- 可调整 ----------
HIDDEN_SIZE = 4     # 隐藏层神经元数量，越大模型容量越高，可尝试 2 / 4 / 8 / 16
# ----------------------------

model = SimpleNN(input_size=2, hidden_size=HIDDEN_SIZE, output_size=1)
print(model)
print(f'\n参数总量: {sum(p.numel() for p in model.parameters())}')
LEARNING_RATE = 0.005   # 学习率，可尝试 0.001 / 0.01 / 0.05
NUM_EPOCHS    = 1000    # 训练轮数，可尝试 500 / 1000 / 2000

# 损失函数：MSELoss 适合回归/直接输出；BCELoss 需要先过 Sigmoid
criterion = nn.MSELoss()        # 可换成 nn.BCELoss()（需在模型中启用 sigmoid）

# 优化器：SGD 最基础；Adam 收敛更快
optimizer = optim.SGD(model.parameters(), lr=LEARNING_RATE)
# optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)  # 可取消注释试试
# ============================


def train_model(model, train_loader, criterion, optimizer, num_epochs):
    """训练模型，每 10% 进度打印一次 Loss"""
    loss_history = []
    log_interval = max(1, num_epochs // 10)

    for epoch in range(num_epochs):
        model.train()
        for inputs, labels in train_loader:
            outputs = model(inputs)
            loss = criterion(outputs, labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        loss_history.append(loss.item())
        if (epoch + 1) % log_interval == 0:
            print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')
def test_model(model, X_test, y_test):
    """评估模型准确率并返回原始预测值"""
    model.eval()
    with torch.no_grad():
        outputs   = model(X_test)
        predicted = (outputs > 0.5).float()     # 可调整阈值，默认 0.5
        accuracy  = predicted.eq(y_test.view_as(predicted)).sum().item() / len(y_test)
        print(f'Test Accuracy: {accuracy:.4f}')
        return outputs


X_tensor = torch.tensor(X_train)
y_tensor = torch.tensor(y_train, dtype=torch.float32).view(-1, 1)

predicted_raw = test_model(model, X_tensor, y_tensor).flatten()
print('predicted (raw) :', predicted_raw.numpy().round(4))
print('predicted (0/1) :', (predicted_raw > 0.5).float().numpy())
print('true            :', y_train)
def visualize_results(X, y_true, y_pred_raw, loss_history):
    """左：Loss 曲线  右：预测结果散点图"""
    y_pred = (y_pred_raw > 0.5).float().numpy()

    fig, axes = plt.subplots(1, 2, figsize=(9, 3.5))

    # --- 左：Loss 曲线 ---
    ax = axes[0]
    ax.plot(loss_history, color='steelblue', linewidth=1.2)
    ax.set_title('Training Loss')
    ax.set_xlabel('Epoch')
    ax.set_ylabel('Loss')
    ax.grid(True, alpha=0.4)

    # --- 右：预测散点图 ---
    ax = axes[1]
    ax.scatter(X[y_pred == 0][:, 0], X[y_pred == 0][:, 1],
               label='Pred 0', color='#4C72B0', s=80, edgecolors='white')
    ax.scatter(X[y_pred == 1][:, 0], X[y_pred == 1][:, 1],
               label='Pred 1', color='#DD8452', s=80, edgecolors='white')
    # 在点旁边标出真实标签
    for i, (xi, yi_true) in enumerate(zip(X, y_true)):
        ax.annotate(f'y={int(yi_true)}', xi, textcoords='offset points',
                    xytext=(6, 4), fontsize=8, color='gray')
    ax.set_title('XOR Dataset (colored by prediction)')
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.legend(loc='upper right', fontsize=9)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


visualize_results(X_train, y_train, predicted_raw, loss_history)