def build_profile(first, last, **user_info):
    profile = {'first_name': first, 'last_name': last}
    for key, value, in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('a', 'b', location='wuhan', filed='math')
print(user_profile)
