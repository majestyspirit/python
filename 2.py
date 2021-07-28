
def thesaurus(*args):
    
    names = {}
    for i in sorted(args):
        if i[0] not in names:
            names[i[0]] = list(filter(lambda el: el.startswith(i[:1]), args))
    print(names)


thesaurus('Mary', 'Ruslan', 'Mihael', 'Alex')
