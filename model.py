import torch.tensor
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from torch import tensor

num_processed = 1
num_ks_1 = 50
k_size_1 = 100
num_ks_2 = 30
k_size_2 = 500
pool_1 = 100

nn_input_size = 200000
hid_layers_1_num = 100
hid_layers_2_num = 10
num_genres = 2


class ConvClassifier(nn.Module):
    def __init__(self):
        '''Model Archetecture: 2 1D conv layers with 1 maxpooling in between'''
        super(ConvClassifier, self).__init__()
        self.conv1 = nn.Conv1d(num_processed, num_ks_1, k_size_1)
        self.pool1 = nn.MaxPool1d(pool_1)
        self.conv2 = nn.Conv1d(num_ks_1, num_ks_2, k_size_2)
        self.fc1 = nn.Linear(nn_input_size, hid_layers_1_num)
        self.fc2 = nn.Linear(hid_layers_1_num, hid_layers_2_num)
        self.fc3 = nn.Linear(hid_layers_2_num, num_genres)

    def forward(self, x):
        dummy_layer = nn.Linear(nn_input_size, num_genres).float()
        x = dummy_layer(x.float())
        x = F.softmax(x)
        return x