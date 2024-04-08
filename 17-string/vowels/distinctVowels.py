
class Solution:
    def countVowels(self,s: str) ->list[list, int]:
        "Counts and return the distinct vowel characters in string s"
        vowels = ["e","i","o","a","u"]
        new_list = []
        count = 0
        for letter in s:
            if letter.lower() in vowels and letter.lower() not in new_list:
                new_list.append(letter.lower())
                count +=1
        return count,new_list

if __name__ =="__main__":
    solution = Solution()
    s = input("Enter a string: ")
    vowel_count, distinct_vowels = solution.countVowels(s)
    print("Number of distinct vowels:", vowel_count)
    print("Distinct vowels:", distinct_vowels)
