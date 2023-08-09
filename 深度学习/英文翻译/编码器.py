import torch.nn as nn


# 定义Encoder
class EncoderRNN(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(EncoderRNN, self).__init__()
        self.hidden_size = hidden_size
        # 词嵌入
        self.embedding = nn.Embedding(input_size, hidden_size)
        