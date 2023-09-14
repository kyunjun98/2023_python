# 주석표현

# 자료형 (DataType) :  숫자형, 문자열, 리스트, 튜플, 딕셔너리, 집합, 불린

# 1) 숫자형 (정수형(integer), 실수 (부동소수점))
# 정수 : 123
# 실수 : 123.45

num01 = 124 ; # long형이 따로 없이 모든 정수는 int형으로 담을 수 있다.
print(num01);
num01 = -124 ; # long형이 따로 없이 모든 정수는 int형으로 담을 수 있다.
print(num01);

num02 = 12.574 ;
print(num02);

# 여러줄 주석 (''' , """)
'''
  숫자연산 : 사칙연산(+,-,*,/)을 계산기와 마찬가지로 사용
  % : 나머지값을 반환
  // : 소숫점 자리를 버리는 연산자 (몫)
'''
su1 = 7 ;
su2 = 3 ;
print(su1/su2);
print(su1%su2);  # 나머지
print(su1//su2); # 몫


# 2) 문자열 : 작은따옴표 사용가능 : 'Hello Python' ;
#            큰따옴표 사용가능 : "Hello Python" ;
# 파이썬에서는 문자형은 없다. 문자열로 표현한다.
# 여러줄 문자열 표현 : ''',  """
print('''
  안녕하세요~~
  Hi~~~
  방가방가~~
''')
print("*"*15)
print("""
  안녕하세요~~
  Hi~~~
  방가방가~~
""");

# 파이썬에서는 문자열을 더하고 곱할 수 있다.
# [문자열 더하기 ] 문자열 + 문자열
# [문자열 곱하기]  문자열 * 숫자 => 해당 문자열을 숫자만큼 반복한다.

s1 = "Hello" ;
k1 = "홍길동";

print (s1 + k1);
print(s1 * 10);

# 문자열에는 인덱싱과 슬라이싱 이 존재한다.
# 인덱싱은 위치에 존재하는 문자열을 추출
# 슬라이싱은 문자열을 나눠서 처리하는 것
print("+" * 20);

str = "문자열에는 인덱싱과 슬라이싱 이 존재한다."
print(str[4])
print("+" * 20);
print(str[0])
print(str[-1])
print(str[-2])
print("+" * 20);

print(str[0:]) # 처음부터 끝까지
print(str[4:]) # 인덱스 4부터 끝까지

print(str[4:7]) # 인덱스 4부터 6까지(7은 포함하지 않음)
print(str[:4]) #  시작부터 3까지 (4는 포함하지 않음)
print("+" * 20);

print(str)
print(str[:])






















