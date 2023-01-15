db = {}

with open('db.csv', encoding='utf-8') as f:
    teachers = [t.strip() for t in f.readline().split(';')][1::]
    for line in f:
        row = [t.strip() for t in line.split(';')]
        class_ = row.pop(0)
        teachs = []
        mp = map(int, row)
        for i in range(len(row)):
            if next(mp):
                teachs.append(teachers[i])
        db[class_] = teachs
