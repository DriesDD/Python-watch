
class presentation:
    def __init__(self):
        self.__counter = 0
        print('Contents:')

    def next(self,topic):
        self.__counter += 1
        print (self.__counter, topic)

watch = presentation()

watch.next('Why learn python?')
watch.next('Installing python')
watch.next('Example 1: watch.py')
watch.next('Example 2: guess.py')
watch.next('Example 3: evomatrix.py')
watch.next('Python in web development')