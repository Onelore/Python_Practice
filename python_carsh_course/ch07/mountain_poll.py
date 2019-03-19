responses = {}
# 设置一个标志，指出调查是否继续
polling_active = True
while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\nWhat's your name?")
    response = input("Which mountain would you like to clime someday?")
    responses[name] = response
    repeat = input("Would you like to let another person respond?(yes or no)")
    if repeat == 'no':
        polling_active = False
print("\n--------Poll Result---------")
for name, response in responses.items():
    print(name + " would like to climb " + response)
