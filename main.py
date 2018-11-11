import os
import torch
from torch.utils.data import DataLoader
import numpy as np
from dataset import SongDataset
from model import ConvClassifier

def evaluate(model, val_loader):
    total_corr = 0
    for i, batch in enumerate(val_loader) :
        feats, label = batch
        feats = feats.permute(2, 0, 1)

        predictions = model.forward(feats)
        predictions = np.argmax((predictions.detach().numpy()), axis=1)
        b = (predictions == label)
        corr_num = int(b.sum())
        total_corr += corr_num
    return float(total_corr)/len(val_loader.dataset)


data_filepath = "./processed_data/final_data"

batch_size = 2
learn_rate = 0.8
MaxEpochs = 100
eval_every = 2

train_data = SongDataset(os.path.join(data_filepath, "train_data.npy"), os.path.join(data_filepath, "train_labels.npy"))
val_data = SongDataset(os.path.join(data_filepath, "val_data.npy"), os.path.join(data_filepath, "val_labels.npy"))
train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True)
val_loader = DataLoader(val_data, batch_size=batch_size, shuffle=False)

model = ConvClassifier()
loss_fnc = torch.nn.BCELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learn_rate)

leftover = 0
step_list = []
train_data_list = []
val_data_list = []
best_val_acc = 0

tot_corr = 0
for counter, epoch in enumerate(range(MaxEpochs)):
    for i, batch in enumerate(train_loader):
        feats, label = batch
        optimizer.zero_grad()

        predictions = model.forward(feats)
        batch_loss = loss_fnc(input=predictions.float(), target=label.float())
        batch_loss.backward()
        optimizer.step()

        predictions = np.argmax((predictions.detach().numpy()), axis=1)  #Both prediction and label 1xnum_genre vectors
        label = np.argmax((label.detach().numpy()), axis=1)
        b = (predictions == label)
        corr_num = int(b.sum())
        tot_corr += corr_num

        # #Evaluate and log losses and accuracies for plotting
        # if (((i + leftover) % eval_every == 0)  and ((i + leftover) != 0)):
        #     val_acc = evaluate(model, val_loader)
        #     train_acc = float((tot_corr) / (eval_every * batch_size))
        #     print("Batch", i, ": Total correct in last", eval_every, "batches is", tot_corr ,
        #           "out of ", eval_every * batch_size)
        #     print("Total training accurracy over last batches is ", train_acc)
        #     print("Total validation accurracy over last batches is ", val_acc, "\n")
        #
        #     # Record relevant values
        #     if len(step_list) == 0:
        #         step_list.append(0)
        #     else:
        #         step_list.append(step_list[-1] + eval_every)
        #
        #     train_data_list.append(train_acc)
        #     val_data_list.append(val_acc)
        #     tot_corr = 0
