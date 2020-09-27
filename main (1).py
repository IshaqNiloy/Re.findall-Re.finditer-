# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
class Regex():
    def __init__(self, string):
        self.string = string

    def find_the_substring(self):
        substring_list = re.findall('[bcdfghjklmnpqrstvwxyz][aeiou][aeiou]+[bcdfghjklmnpqrstvwxyz]',string,re.I)

        if len(substring_list) > 0:
            for substring in substring_list:
                print(substring[1:-1])
        else:
            print(-1)


if __name__ == '__main__':
    string = input()
    my_object = Regex(string)
    my_object.find_the_substring()
