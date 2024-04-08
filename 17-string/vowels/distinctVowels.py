
class Solution:
    def countVowels(self,s):
        vowels = ["e","i","o","a","u"]
        new_list = []
        count = 0
        for letter in s:
            if letter in vowels and letter not in new_list:
                new_list.append(letter)
                count +=1
        return count,new_list


if __name__ =="__main__":
    solution = Solution()
    s = input("Enter a string: ")
    result = solution.countVowels("aHMAD")
    print(result)