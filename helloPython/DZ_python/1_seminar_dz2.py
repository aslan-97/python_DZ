#Напишите программу для проверки ложности утверждения
#(W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W)

print("z y w x")
for z in range (2):
    for y in range (2):
        for w in range (2):
            for x in range (2):
                if (x and z) or not y or (not x == w):
                    print(z, y, w, x )