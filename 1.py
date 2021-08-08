with open('nginx_logs', 'r', encoding='utf-8') as file_1:
    lines = ((line.split()[0], line.split()[5][1:], line.split()[6]) for line in file_1)
    for i in lines:
        print(i)
