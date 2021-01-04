import matplotlib.pyplot as plt


def display_plots(ot1File, ot2File, image1, image2):

    dict1 = {}
    dict2 = {}
    with open(ot1File, 'r') as file1:

        data1 = file1.read()
        data1 = data1.split('\n\n')[:-1]
        for element in data1:

            params = element.split(' --- ')
            hash1, hash2, prf, time = params[0], params[1], params[2], params[3]
            dict1[hash1+' '+hash2+' '+prf]=time

    with open(ot2File, 'r') as file2:

        data2 = file2.read()
        data2 = data2.split('\n\n')[:-1]
        for element in data2:
            params = element.split(' --- ')

            hash1, hash2, prf, time = params[0], params[1], params[2], params[3]
            dict2[hash1 + ' ' + hash2 + ' ' + prf] = time

    ticks = list(range(len(dict1.keys())))

    names1 = list(dict1.keys())
    values1 = list(dict1.values())
    values1.sort()
    names1 = []

    for value in values1:
        for x in dict1:
            if dict1[x]== value:
                names1.append(x)
                break
    print(names1)

    names2 = list(dict2.keys())
    values2 = list(dict2.values())
    values2.sort()
    names2 = []

    for value in values2:
        for x in dict2:
            if dict2[x]== value:
                names2.append(x)
                break
    print(names2)

    import matplotlib
    matplotlib.rc('xtick', labelsize=4.8)

    plt.figure(figsize=(20, 20))
    plt.scatter(names1, values1)
    plt.xticks(names1, names1, rotation=90)

    plt.savefig(image1)

    plt.figure(figsize=(20, 20))
    plt.scatter(names2, values2)
    plt.xticks(names2, names2, rotation=90)

    plt.savefig(image2)

display_plots('statisticsOt1.txt', 'statisticsOt2.txt', 'ot1.png', 'ot2.png')
