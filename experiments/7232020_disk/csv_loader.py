import torch

import csv


class CSVDataset(torch.utils.data.Dataset):
    """
    PyTorch dataset for CSV format with the following rows:
    x,y,z,..., class. I.e. a list of coordinates followed by a class.
    Entire dataset is loaded into memory at runtime, so can't be too huge.
    """
    def __init__(self, file, device='cpu'):
        with open(file) as csvfile:
            csv_data = list(csv.reader(csvfile, delimiter=','))
            for i in range(len(csv_data)):
                for j in range(len(csv_data[1])):
                    if i != 0:
                        csv_data[i][j] = float(csv_data[i][j])
            self.csv_tensor = torch.tensor(csv_data[1:]).float().to(device)
        
    def __len__(self):
        return self.csv_tensor.shape[0]
    
    def __getitem__(self, index):
        # input, output
        return self.csv_tensor[index][:-1], self.csv_tensor[index][-1].long()
