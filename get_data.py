import os

labelMap={"negative":0,"neutral":1,"positive":2}

def main():
    data_dir = "./实验五数据/"
    train_file = os.path.join(data_dir, "train.txt")
    assert os.path.isfile(train_file), "Train data not found at %s" % train_file
    test_file = os.path.join(data_dir, "test_without_label.txt")
    assert os.path.isfile(test_file), "Test data not found at %s" % test_file
    # 先处理train.txt
    fin = open(train_file, 'r', encoding='utf-8', newline='\n', errors='ignore')
    lines = fin.readlines()
    # 共有4000个元素，训练集验证集3700:300

    # 处理训练集
    f = open(os.path.join(data_dir, "train.tsv"), "w", encoding='utf-8')
    f.write("index\t#1 Label\t#2 ImageID\t#3 String\t#3 String\n")
    count = 0
    for i in range(1, 3700):
        count += 1
        guid = lines[i].strip()
        guid, tag = guid.split(",")
        file1 = "./实验五数据/data/" + guid + ".txt"
        fin_text = open(file1, 'r', encoding='gb18030')
        lines_text = fin_text.readlines()
        text = ""
        for i in range(0, len(lines_text)):
            text += lines_text[i].strip() + "\t";
        polarity = labelMap[tag]
        imgid = guid
        label = str(int(polarity))
        f.write("%d\t%s\t%s\t%s\n" % (count, label, imgid, text))

    # 验证集
    dev_f = open(os.path.join(data_dir, "dev.tsv"), "w", encoding='utf-8')
    dev_f.write("index\t#1 Label\t#2 ImageID\t#3 String\t#3 String\n")
    count = 0
    for i in range(3700, len(lines)):
        count += 1
        guid = lines[i].strip()
        guid, tag = guid.split(",")
        file1 = "./实验五数据/data/" + guid + ".txt"
        fin_text = open(file1, 'r', encoding='gb18030')
        lines_text = fin_text.readlines()
        text = ""
        for i in range(0, len(lines_text)):
            text += lines_text[i].strip() + "\t";
        polarity = labelMap[tag]
        imgid = guid
        label = str(int(polarity))
        dev_f.write("%d\t%s\t%s\t%s\n" % (count, label, imgid, text))

    # 测试集
    fin_test = open(test_file, 'r', encoding='utf-8', newline='\n', errors='ignore')
    lines_test = fin_test.readlines()
    test_f = open(os.path.join(data_dir, "test.tsv"), "w", encoding='utf-8')
    test_f.write("index\t#1 Label\t#2 ImageID\t#2 String\t#2 String\n")
    count = 0
    for i in range(1, len(lines_test)):
        count += 1
        guid = lines_test[i].strip()
        guid, tag = guid.split(",")
        file1 = "./实验五数据/data/" + guid + ".txt"
        fin_text = open(file1, 'r', encoding='gb18030')
        lines_text = fin_text.readlines()
        text = ""
        for i in range(0, len(lines_text)):
            text += lines_text[i].strip() + "\t";
        imgid = guid
        label = tag
        test_f.write("%d\t%s\t%s\t%s\n" % (count, label, imgid, text))
    print("\tCompleted!")

if __name__ == '__main__':
    main();