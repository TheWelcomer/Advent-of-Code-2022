with open("data.txt", 'r') as f:
    lines = f.read().split('\n\n')
    seeds = lines[0].strip('\nseeds: ').split(' ')
    seeds = list(map(lambda x: int(x), seeds))
    result = float('inf')
    objs = []
    for i in range(1, len(lines)):
        strobj = lines[i].split('\n')
        obj = {}
        for j in range(1, len(strobj)):
            mapping = strobj[j].split(' ')
            mapping = list(map(lambda x: int(x), mapping))
            obj[(mapping[1], mapping[1] + mapping[2] - 1)] = mapping[0]
        objs.append(obj)
    for i in range(0, len(seeds), 2):
        start, reps = seeds[i], seeds[i + 1]
        j = start
        
        while j < start + reps:
            seed = j
            skips = float('inf')
            for obj in objs:
                for key in obj.keys():
                    if seed >= key[0] and seed <= key[1]:
                        skips = min(skips, (key[1] - seed) + 1)
                        seed = obj[key] + (seed - key[0])
                        break
            j += skips            
            result = min(result, seed)
    print(result)
    # one.py slow solution
        
    # for seed in seeds:
    #     for obj in objs:
    #         for key in obj.keys():
    #             if seed >= key[0] and seed <= key[1]:
    #                 seed = obj[key] + (seed - key[0])
    #                 break
    #     result = min(result, seed)
    # print(result)