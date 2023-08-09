import threading
nums = list(range(100))
def p(nums):
    for num in nums:
        print(num)
threads = []
for i in range(5):
    t = threading.Thread(target=p,args=(nums[i*20:(i+1)*20],))
    t.start()