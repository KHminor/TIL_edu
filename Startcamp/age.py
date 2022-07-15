import requests
name = input("이름을 입력하세요: ")
url = 'https://api.agify.io/?name={}'.format(name)
# response = requests.get(url)
response = requests.get(url).json()
print(response)
name = response['name']
age = response['age']
count = response['count']

print('이름이 '+ name + '인 사람의 나이는 ' + str(age) + '입니다')