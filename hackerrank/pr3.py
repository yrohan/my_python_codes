def cookies(k, A):
    print(A)
    print(k)
    sorted_A = sorted(A)
    sum_A = sorted_A[0] + sum([2 * sorted_A[i] for i in range(1, len(sorted_A))])
    if sum_A < k:
        return -1
    else:
        val = [x for x in sorted_A if x < k]
        print(val)
        return 1


if __name__ == '__main__':
    input_file = open('input.txt','r')
    first_multiple_input = input_file.readline().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    A = list(map(int, input_file.readline().rstrip().split()))
    result = cookies(k, A)
    print(result)

'''1,2,3,4,5,6,7,8,9
3,3,4,5,6,7,8,9
6,4,5,6,7,8,9
6,9,6,7,8,9
12,9,7,8,9
15,12,9,9
15,12,18'''