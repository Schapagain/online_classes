
def heapify(heap):
    responseList = []
    firstNonLeaf = len(heap)//2 - 1
    for i in range(firstNonLeaf,-1,-1):
        bubbleDown(heap,i,responseList)
    
    print(heap)
    return responseList


def bubbleDown(heap,i,responseList):
    while True:
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(heap) and heap[left] < heap[smallest]:
            smallest = left
        if right < len(heap) and heap[right] < heap[smallest]:
            smallest = right      
        
        # if the root of sub-tree is the smallest, no further swaps needed
        if smallest == i: break

        # else swap and increment swap count by 1
        heap[smallest], heap[i] = heap[i], heap[smallest]

        print('appending',heap[i],heap[smallest])
        responseList.append([heap[i],heap[smallest]])

        # make the smaller child the subtree in focus
        i = smallest
    
    return responseList


fnames = ["heapify_tests/03"]

for fname in fnames:
    f = open(fname)
    # f_ans = open(fname+'.a')

    all_input = f.read().strip().split('\n')
    vals = list(map(int,all_input[1].split()))
    print(vals)
    my_res = heapify([1,2,3,4,5])
    print(my_res)
    # expected_res_str = f_ans.read().strip().split('\n')
    # if expected_res_str[0] == '':
    #     expected_res = []
    # else:
    #     expected_res = list(map(int,expected_res_str))
    # assert(my_res == expected_res)
print("Everything looks good!")