import torch
import numpy as np
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
import matplotlib.pyplot as plt
import torch.optim as optim
x=torch.tensor([[1.0,0],[1,1],[0,0],[0,1]],dtype=torch.float32)
y=torch.tensor([[1],[0],[0],[1]],dtype=torch.float32)
dataset=TensorDataset(x,y)
dataloader=DataLoader(dataset,batch_size=1,shuffle=False)

class Simple(nn.Module):
    def __init__(self,input_size=2,hidden_size=4,output_size=1):
        super(Simple,self).__init__()
        self.fc1=nn.Linear(input_size,hidden_size)
        self.relu=nn.ReLU()
        self.fc2=nn.Linear(hidden_size,output_size)
    def forward(self,x):
        out=self.fc1(x)
        out=self.relu(out)
        out=self.fc2(out)
        return out

model=Simple()
print(model)

def model_train(model,dataloader,criterion,optimizer,num):
    loss_history=[]
    interval=max(1,num/20)
    for i in range(num):
        model.train()
        for input,label in dataloader:
            output=model(input)
            loss=criterion(output,label)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        loss_history.append(loss.item())
        if (i+1)%interval==0:
            print(f"{i+1}/{num} has finished, loss:{loss.item():.4f}")
    return loss_history

criterion=nn.MSELoss()
optimizer=optim.SGD(model.parameters(),lr=0.01)
loss_history=model_train(model,dataloader,criterion,optimizer,1000)

def test_train(mdoel,x,y):
    model.eval()
    with torch.no_grad():
        output=model(x)
        predicted=(output>0.5).float()
        accuracy=predicted.eq(predicted.view_as(y)).sum().item()/len(y)
        print(f"accuracy:{accuracy}")
        return output

output=test_train(model,x,y)
print(output)

plt.plot(loss_history,color="r",linestyle="-")
plt.grid(True)
plt.xlabel("epoches")
plt.ylabel("loss")
plt.legend()
plt.show()


