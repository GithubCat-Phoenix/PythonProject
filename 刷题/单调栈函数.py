def monotonic_stack(arr):
    stack = []  # 初始化空栈
    res = [-1] * len(arr)  # 初始化结果数组

    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            res[stack.pop()] = i  # 弹出栈顶元素，设置结果
        stack.append(i)  # 当前元素入栈

    return res


if __name__ == "__main__":

    print(monotonic_stack([1,2,9,5,7]))