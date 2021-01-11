
def mergerScript(file1, file2):

    with open(file1, 'r') as filex1:
        content1 = filex1.read()

    with open(file2, 'r') as filex2:
        content2 = filex2.read()

    content1 = content1.split('\n\n')[:-1]
    content2 = content2.split('\n\n')[:-1]
    content1X = [float(x.split(' --- ')[-1]) for x in content1]
    content2X = [float(x.split(' --- ')[-1]) for x in content2]

    def colorCode(timestamp, content):

        contentSorted = sorted(content)
        timestamp = float(timestamp)
        index = contentSorted.index(timestamp)

        if index == 0:
            return 'green'
        elif index in list(range(1,10)):
            return 'cyan'
        elif index in list(range(10,30)):
            return 'yellow'
        elif index in list(range(30,50)):
            return 'orange'
        else:
            return 'red'


    for content in zip(content1, content2):
        base  = content[0].rsplit(' --- ', 1)[0]
        timestamp1 = content[0].rsplit(' --- ', 1)[1]
        timestamp2 = content[1].rsplit(' --- ', 1)[1]
        base = base.replace(' --- ', ' & ')
        base = base.replace('_', '\\_')
        base = base + ' & \colorbox{'+colorCode(timestamp1, content1X)+'}{'+ timestamp1+'} & \colorbox{'+colorCode(timestamp2, content2X)+'}{'+timestamp2+'} \\\\\n\\hline\n'
        with open('latex'+file1.split('_')[1].split('.')[0], 'a') as filex:
            filex.write(base)



mergerScript('../statisticsOt1_512.csv.txt', '../statisticsOt2_512.csv.txt')
mergerScript('../statisticsOt1_1024.csv.txt', '../statisticsOt2_1024.csv.txt')
mergerScript('../statisticsOt1_2048.csv.txt', '../statisticsOt2_2048.csv.txt')
mergerScript('../statisticsOt1_4096.csv.txt', '../statisticsOt2_4096.csv.txt')