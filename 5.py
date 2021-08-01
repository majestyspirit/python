src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f'src = {src}')
# print(f'result = {[n for n in src if src.count(n) == 1]}')


res = (src[i] for i in range(len(src)) if src[i] not in src[:i] and src[i] not in src[:i:-1])
print(f'result = {[a for a in res]}')

