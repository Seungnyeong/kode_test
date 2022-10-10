# https://www.acmicpc.net/problem/1517
# 문제에는 동일한 원소가 나오지 않는다는 조건이 없다.
# 즉, 3 2 5 3 4와 같은 경우가 있을 수 있다.
# 이를 고려하여 코드를 작성해야 한다.
# 문제 조건에 따르면 최대 25 * (10^10)의 시간 복잡도를 가진다.
# 파이썬의 1초당 계산 가능 횟수는 2 * (10^7)이므로, 버블 소팅으로는 문제를 풀 수 없다.
# 병합정렬을 이용하면 N * log(N)의 시간복잡도가 소요된다. 
# 5*(10^5) * log(5*(10^5))이므로, 시간 복잡도는 해결이 된다.
 

def mergeSort(start, end):
    global cnt    
    if start < end:
        mid = (start + end) // 2
        mergeSort(start, mid)
        mergeSort(mid + 1, end)

        a = start
        b = mid + 1
        tmp = []
        while a <= mid and b <= end:
            if arr[a] <= arr[b]:
                tmp.append(arr[a])
                a += 1

            else:
                tmp.append(arr[b])
                b += 1
                cnt += (mid - a + 1)  # 스와핑 했을 때 개수추가
        if a <= mid:
            tmp = tmp + arr[a:mid+1]
        if b <= end:
            tmp = tmp + arr[b:end+1]

        for i in range(len(tmp)):
            arr[start + i] = tmp[i]

if __name__ == '__main__':
    cnt = 0
    n, arr = int(input()), list(map(int, input().split()))
    mergeSort(0, n-1)
    print(cnt)