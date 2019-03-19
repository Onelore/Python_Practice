favorite_nums = {
    'jack': ['2', '88', '99'],
    'july': ['7', '92', '21'],
    'bob': ['9', '22'],
    'wu': ['19', '33', '11', '43'],
    'john': ['27', '25']
}
for name, nums in favorite_nums.items():
    print(name.title() + "'s favorite number is :")
    for num in nums:
        print("\t" + num)
