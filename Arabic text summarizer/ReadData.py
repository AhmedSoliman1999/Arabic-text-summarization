import os

def read_data():
    file_list=[]
    Articles=[]
    for i in range(1,2):
        path = r"C:\Users\Engy\PycharmProjects\GP\EASC\EASC-UTF-8\Articles/" + "Topic" + str(i)
        os.chdir(path)
        for x in os.listdir():
            filename = f"{path}\{x}"
            if filename.endswith('.txt') | filename.endswith('.TXT'):
                file_list.append(filename)
                y = open(filename, encoding='utf-8')
                with y as z:
                    Articles.append(z.read())
                y.close()
    return Articles
def read_y():
    file_list = []
    Article = []
    Articles=[]
    k = 101

    for i in range(1, 2):
        Article = []
        l=65
        path = r"C:\Users\Engy\PycharmProjects\GP\EASC\EASC-UTF-8\MTurk\Topic"+ str(i)
        os.chdir(path)
        for x in os.listdir():
            filename = f"{path}\{x}"
            file_list.append(filename)
            y = open(filename, encoding='utf-8')
            with y as z:
                Article.append(z.read())
            y.close()

        Articles.append(Article)
    # print(len(Articles[0]))
    return Articles