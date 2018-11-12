import torch.tensor
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from torch import tensor

num_processed = 1
num_ks_1 = 50
k_size_1 = 500
num_ks_2 = 30
k_size_2 = 100
pool_1 = 100

nn_input_size = 56880  #NOTE - this is hard coded. Will need to be different if song length != 200000
hid_layers_1_num = 100
hid_layers_2_num = 10
num_genres = 2


class ConvClassifier(nn.Module):
    def __init__(self):
        '''Model Archetecture: 2 1D conv layers with 1 maxpooling in between'''
        super(ConvClassifier, self).__init__()
        self.conv1 = nn.Conv1d(num_processed, num_ks_1, k_size_1).float()
        self.pool1 = nn.MaxPool1d(pool_1)
        self.conv2 = nn.Conv1d(num_ks_1, num_ks_2, k_size_2).float()
        self.fc1 = nn.Linear(nn_input_size, hid_layers_1_num)
        self.fc2 = nn.Linear(hid_layers_1_num, hid_layers_2_num)
        self.fc3 = nn.Linear(hid_layers_2_num, num_genres)

    def forward(self, x):
        # dummy_layer = nn.Linear(nn_input_size, num_genres).float()
        # x = dummy_layer(x.float())
        assert (x.shape[1] == 200000)  #Just in case we forget to change nn_input_size
        x = (x.unsqueeze(1)).float()
        x = self.conv1(x)
        #print(x.shape)
        x = self.pool1(x)
        #print(x.shape)
        x = self.conv2(x)
        #print(x.shape)
        x = x.view(3, -1)  #Convert feature maps for each song in batch into 1-d array
        #print (x.shape)
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)
        x = F.softmax(x)
        #print (x.shape)
        return x