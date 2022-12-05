import os

class ShereenKhojaStemmer():

    # Get the article content
    def readContent(article):
        if os.path.exists(article):
            return open(article, 'r', encoding="utf-8").read()

    def stem(self, content):

        jarShereenKhojaSegmenter = os.path.join('.', 'KhojaStemmer.jar')

        tmp = os.path.join('.', 'tmp')
        if os.path.exists(tmp):
            os.system('del ' + tmp)

        open(tmp, 'w', encoding="utf-8").write(content)

        for folder, subs, files in os.walk(('.').encode( 'utf-8')):

            tmpStem = os.path.join('.', 'tmpStem.txt')

        if os.path.exists(tmpStem):
            os.system('del ' + tmpStem)

        os.system('java -Dfile.encoding=UTF-8 -jar ' + jarShereenKhojaSegmenter + ' ' + tmp + ' ' + tmpStem)

        string = self.readContent(tmpStem)

        os.system('del ' + tmpStem)
        os.system('del ' + tmp)
      ##  print("string",string)
        """
        words = string.split()
        stems_list = []
        for word in words:
            # add new stem to dict
            stems_list.append(word)
        """
        return string
