# / // % 를 사용하는 예제 
# https://www.acmicpc.net/problem/5585

# 380
# 4

# 1
# 15

remain = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]

whole_coin_count = 0

for coin in coins:
  # coin_count = remain//coin
  # whole_coin_count += coin_count
  
  whole_coin_count += remain//coin
  
  # remain = remain - coin_count * coin
  remain %= coin

print(whole_coin_count)