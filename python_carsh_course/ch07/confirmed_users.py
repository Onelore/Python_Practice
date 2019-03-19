# 创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表\
unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []

# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的列表都转移到已验证列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# 显示所以验证用
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print("\t" + confirmed_user.title())
