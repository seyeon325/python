# 사용자에게 숫자 입력 받기
num = int(input("숫자를 입력 => "))

# 짝수 홀수 판별

# <- 100/ 100~ 1000/ 1000->
# 1. 100 이하 조건
# 2. 1000 이하 조건


if num < 1000:
    print("1000보다 작음")
else:
    if num < 100:
        print("1000보다 작고 , 100보다 큼")
    else:
        print("100 보다 작음")


if num < 100:
    print("100보다 작음")
else:
    if num < 1000:
        print("100보다 크고, 1000보다 작음")
    else:
        print("1000보다 큼")
    