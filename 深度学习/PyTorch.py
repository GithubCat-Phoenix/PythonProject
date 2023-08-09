import torch


def test01():
    data = torch.randint(0, 10, [4, 5])
    print(data)
    print('-'*30)
    print(data[1:, 1])


if __name__ == '__main__':
    test01()