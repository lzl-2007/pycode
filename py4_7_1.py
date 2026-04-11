import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader,TensorDataset
import numpy as np
import matplotlib.pyplot as plt

torch.manual_seed(12)
x=torch.randn(500)
y=x**2
dataset=TensorDataset(x,y)
dataloader=DataLoader(dataset,batch_size=1,shuffle=True)


class two(nn.Module):
    def __init__(self,input_size=1,hidden_size=5,out_size=1):
        super(two,self).__init__()
        self.fc1=nn.Linear(input_size,hidden_size)
        self.fc2=nn.ReLU()
        self.fc3=nn.Linear(hidden_size,out_size)
    def forward(self,x):
        out=self.fc1(x)
        out=self.fc2(out)
        out=self.fc3(out)
        return out

model=two()

def model_train(model,trainloader,criterion,optimizer,epoch_num):
    
    loss_history=[]
    interval=max(1,epoch_num/10)
    for i in range(epoch_num):
        model.train()
        for input,label in trainloader:
            output=model(input)
            loss=criterion(output,label)
            optimizer.zero_grad()
            
            loss.backward()
            optimizer.step()
        loss_history.append(loss.item())
        if (i+1)%interval==0:
            print(f"{i+1}/{epoch_num}has finished,loss: {loss.item()}")
    return 0


lr=0.01
epochnum=100
optimizer=optim.SGD(model.parameters(),lr=lr)
model_train(model,dataloader,nn.MSELoss(),optimizer,epochnum)

torch.manual_seed(10)
x_test=torch.arange(-1,1,0.05)
with torch.no_grad():
    y_test=model(x_test.reshape(-1,1))
criterion=nn.MSELoss()
loss=criterion(x_test,y_test)
plt.scatter(x_test,y_test,color="r",marker="*",label=f"lr={lr},epochnum={epochnum}")
plt.xlabel("x")
plt.plot(x_test,x_test**2,color="skyblue",label=f"y=x^2,loss={loss:.2f}")

plt.ylabel("y")
plt.legend(loc="best")
plt.show()




