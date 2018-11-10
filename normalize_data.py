import os
import numpy as np

def find_cummu_avg(all_data):
    '''
    Find avergae value over each row in all_data

    :return all_data sized array: averages that shpuld be subtracted: 
    '''
    normalizers = all_data.sum(axis=1)
    normalizers = np.divide(normalizers, all_data.shape[1])
    normalizers = np.expand_dims(normalizers, axis=1)
    # normalizers = np.expand_dims(normalizers, 2)
    # normalizers = np.repeat(normalizers, 100, axis=2)
    # normalizers = np.moveaxis(normalizers, 2, 0)
    return normalizers

def find_cummu_std(all_data, avg):
    '''
    Find std over each row in all_data
    '''
    cummu_var = (np.power(all_data - avg, 2)).sum(axis=1)
    std = np.power(np.divide(cummu_var, all_data.shape[1]), 0.5)
    std = np.expand_dims(std, 1)
    return std


def normalize_data(data_file) :
    '''Normalize each row in data array by subtracting mean and dividing my std.'''
    all_data = np.load(data_file)
    avg = find_cummu_avg(all_data)
    std = find_cummu_std(all_data, avg)
    norm = np.divide((all_data - avg), np.repeat(std, all_data.shape[1], axis=1))

    file_name = (data_file.split("."))[0]
    np.save(file_name + "_normalized", norm)  # Saves without time col

if __name__ == "__main__":
    normalize_data("rock_songs.npy")