# def cat_n_time(s, n):
#     while s != 0:
#         print(n)
#         s = s - 1
# text = input('what would you like the computer to repeat to you: ')
# num = input('how many times: ')
# cat_n_time(int(num), text)

def cat_n_times(s, n):
    for i in range(n):
        print(s)
text = input('what would you like the computer to repeat back to you: ')
num = int(input('how many times: '))

cat_n_times (text, num)
