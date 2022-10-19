shoolboy = [{input() for a in range(int(input()))}
            for b in range(int(input()))]
known_everyone = set.intersection(*shoolboy)
#языки которые знают все школьники,set.intersection(пересечение)(элементы которые есть в нескольких списках)
known_someone = set.union(*shoolboy)
#языки которые знает хотя бы один,set.union(обьединение)(уникальные элементы)
print(len(known_everyone), *sorted(known_everyone), sep='\n')
print(len(known_someone), *sorted(known_someone), sep='\n')
