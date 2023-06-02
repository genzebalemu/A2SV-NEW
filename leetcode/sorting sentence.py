class Solution(object):
    def sortSentence(self, s):
        list_1 = s.split()
        # return list_1

        for i in range(0,len(list_1)):
            min_index=i
            for j in range(i+1,len(list_1)):
                if list_1[min_index][-1] > list_1[j][-1]:
                    min_index=j

            list_1[i],list_1[min_index]=list_1[min_index],list_1[i]
            list_1[i] = list_1[i][: -1]
        # res = [sub[: -1] for sub in list_1]
            

        listToStr = ' '.join([str(elem) for elem in list_1])
        return listToStr

      