#jelenitsuk meg ket lista kozotti kulonbsegeket

list1 = [1, 2, 3, 4, "Alma", "Korte", "Szilva", "Barack"]
list2 = [1, 2, "Korte"]

print(list(set(list1) - set(list2)))
