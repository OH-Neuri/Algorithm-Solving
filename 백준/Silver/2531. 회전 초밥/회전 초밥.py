import sys
input = sys.stdin.readline
##############################################
n, d, k, c = map(int, input().split())

# 레일 위의 스시를 나타내는 리스트
sushi = []
for _ in range(n):
    sushi.append(int(input()))

# d종류의 스시에 대해서 선택한 연속된 k에 포함된 개수
check_dish = [0 for _ in range(d+1)]


# 처음부터 k개의 접시를 고른 경우
count = 0
for i in range(k):
    # 만약 이번에 추가된 접시가 이전에 고른 스시가 아닌경우 개수 추가
    if check_dish[sushi[i]] == 0:
        count += 1
    check_dish[sushi[i]] += 1

    # count의 최대값이 저장될 변수
    # 쿠폰 스시 포함 여부에 따라 개수를 추가하여 초기화
    if check_dish[c] == 0:
        answer = count + 1

    else:
        answer = count


# 초기 상태에서 다음 접시를 추가하고 첫 접시를 제거
# 0~k-1번까지 k개 고른뒤 k번째 접시를 넣고, 0번째 접시를 제거
for i in range(k, n + k - 1):
    # 만약 이번에 추가된 접시가 이전에 고른 스시가 아닌경우 개수 추가
    if check_dish[sushi[i % n]] == 0:
        count += 1
    check_dish[sushi[i % n]] += 1

    # 이번에 빠진 스시가 1개만 있었으면 개수 빼기
    if check_dish[sushi[i - k]] == 1:
        count -= 1

    check_dish[sushi[i - k]] -= 1

    # 쿠폰으로 받는 스시가 지금 고른 접시중에 포함 안되어 있으면
    # count +1개와 answer를 비교해서 갱신
    if check_dish[c] == 0:
        answer = max(answer, count + 1)

    # 아니면 그냥 갱신
    else:
        answer = max(answer, count)

# count 최댓값 출력
print(answer)