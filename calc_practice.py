# / // % 를 사용하는 예제 
# https://www.acmicpc.net/problem/5585

# 380
# 4

# 1
# 15


a = input()
remain = 1000-int(a)
coin_500 = remain//500
remain = remain-(coin_500 * 500)
coin_100 = remain//100
remain= remain-(coin_100 *100)
coin_50 = remain//50
remain= remain-(coin_50 *50)
coin_10 = remain//10
remain= remain-(coin_10 *10)
coin_1 = remain//1 








