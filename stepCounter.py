def main():
    posSteps = []
    n = 0
    while(n < 2):
        n = int(input('Enter the number of stairs (n): '))

    while(len(posSteps) < n):
        step = int(input('Enter a possible step to be taken(Enter 0 when done): ' ))
        if(step == 0):
            if(len(posSteps) >= 2):
                break
            else:
                print('Need at least 2 possible steps.')
                continue
                
        elif step in posSteps:
            print('Must be a new number')
            continue
        
        elif((step < 0) or (step > n)):
            print('Must be between 1 and n')
            continue
        
        else:
          posSteps.append(step)

    posSteps.sort()
    countPaths(n, posSteps)


##Calculate n for all steps
def countPaths(n, posSteps):
    count = [0] * n

    #aps = [[[]for x in range(0, n)] for y in range(0, n)]
    aps = [[]] * n
    print(aps)

    ##initialize possible steps as 1
    for elem in posSteps:
        count[elem-1] = 1
        aps[elem-1].append(elem)
    print(aps)
                
    ##add up steps to calculate later steps
    for x in range(0, n):
        for y in range(0, len(posSteps)):
            ##Do not add steps that do not exist (step 1 + step-4)
            if(((x+1)-posSteps[y]) > 0):
                count[x] += count[x-(posSteps[y])]
                aps[x-posSteps[y]].append(posSteps[y])
                aps[x].append(aps[x-posSteps[y]])
        print(x+1, ": ", aps[x])
                
    ##print n for all steps
    ##for x in range(0, len(count)):
        #print("stair",  x+1, " = ", count[x])
    

    ##prints only the given step
    #return count[n]

if(__name__ == "__main__"):
    main();
