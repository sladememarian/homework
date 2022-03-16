import random as rnd
p_s = 200
n = 100
m_r = 0.8 # mutation rate
epoch = 200
def init_population(population_size, n):
    population_list = []
    for i in range(population_size):
        new_member = []
        for j in range(n):
            new_member.append(rnd.randint(1,n))
        new_member.append(0)
        population_list.append(new_member)
    return population_list

def crossover(population_list):
    # new_population = []
    for i in range(0, len(population_list), 2):
        child = population_list[i][:len(population_list[0])//2] + population_list[i+1][len(population_list[0])//2:len(population_list[0])-1] + [0]
        child2 = population_list[i+1][:len(population_list[0])//2] + population_list[i][len(population_list[0])//2:len(population_list[0])-1] + [0]
        population_list.append(child)
        population_list.append(child2)
    return population_list

def mutation(population_list, mutation_rate, n):
    chosen_members = [i for i in range(len(population_list)//2, len(population_list))]
    for i in range(len(population_list)//2):
        new_rand = rnd.randint(0, (len(population_list)//2)-1)
        chosen_members[new_rand] = chosen_members[i]
        chosen_members[i] = chosen_members[new_rand]
    chosen_members = chosen_members[:int(len(chosen_members)*mutation_rate)]
    for i in chosen_members:
        new_ch = rnd.randint(0, n-1)
        new_ch_value = rnd.randint(1, n)
        population_list[i][new_ch] = new_ch_value
    return population_list

def fitness(population_list, n):
    i = 0
    conflict = 0
    while i < len(population_list):
        j = 0
        conflict = 0
        while j < n:
            l = j+1
            while l < n:
                if population_list[i][j] == population_list[i][l]:
                    conflict += 1
                if abs(j-l) == abs(population_list[i][j]-population_list[i][l]):
                    conflict += 1
                l += 1
            j += 1
        population_list[i][len(population_list[j])-1] = conflict
        i += 1
    
    for i in range(len(population_list)):
        _min = i
        for j in range(i, len(population_list)):
            if population_list[j][n] < population_list[_min][n]:
                _min = j
        population_list[i], population_list[_min] = population_list[_min], population_list[i]
    return population_list




population = init_population(p_s, n)
population = fitness(population, n)
if population[0][n] == 0:
    print("Solution found")
    print(population[0][0:n])
else:
    for i in range(epoch):    
        population = crossover(population)
        population = mutation(population, m_r, n)
        population = fitness(population, n)
        population = population[:len(population)//2]
        if population[0][n] == 0:
            print("Solution found:")
            print(population[0][0:n])
            break
        else :
            print(f"Epoch: {i+1} conflict:", population[0][n])


# for i in population:
#     print(i)