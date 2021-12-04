# 문제 정의
# 한 마을에 모험가가 N명 있다. 모험가 길드에서는 N명의 모험가를 대상으로 공포도를 측정했는데, 공포도가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어진다.
# 모험가 길드장인 동빈이는 모험가 그룹을 안전하게 구성하고자 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정했다.
# 동빈이는 최대 몇 개의 모험가 그룹을 만들 수 있는 지 궁금하다. N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 모험가의 수 N이 주어진다. (1 ≤ N ≤ 100,000)
# 둘째 줄에 각 모험가의 공포도의 값을 N 이하의 자연수로 주어지며, 각 자연수는 공백으로 구분한다.

# 출력
# 여행을 떠날 수 있는 그룹 수의 최댓값을 출력한다.

# 입력 예시
# 5
# 2 3 1 2 2

# 출력 예
# 2

#질문0 : 한번에 주석처리하는 법? 단축키 알아보기 

number= int(input("How many memebers are in your guild?"))
terror_list =list(map(int, input("How much terror level does each member have?").split()))

#similar but little different style of inputs(엔터로 구분)
#N=number
#terror_list_b=[]
#for i in range(N): 
#    terror_list_b.append(int(input("Please enter Terror level of each memebr, one by one")))

terror_list_set = set(terror_list)
unique_terror_list = list(terror_list_set)

#def compare(x):
#    if input() >= x :
#        return(1)


#질문1. def 쓸 때 그 내부에서 활용되는 변수는 다른 곳에서 쓰인 변수명 써도 되는가?
def countif(some_list, cond= None):
    if cond:
        count = sum(cond(element) for element in some_list)
    else:
        count = len(some_list)
    return count


possible_combination = 0
for i in unique_terror_list:
    count = countif(terror_list, lambda x: x>= i)
    if count >= i:
        possible_combination += 1

print(possible_combination)


#질문2. 왜 아래처럼 했을 때는 바로 안될까요? 
#for i in unique_terror_list:
#    count = sum(map(lambda x : x >= i, terror_list_set))

 

#연습장
#질문3: number를 받아서 그 number 만큼의 element를 가진 list를 만들어서 거기에 input을 받아서 숫자를 덮어씌울 수 있난가?
#terror_list= [1:number]
#list_a = []
#a = input("By the way, what is your favorite number?")
#list_a.append(a)
#print(list_a)