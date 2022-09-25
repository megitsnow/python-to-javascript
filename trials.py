"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)

def get_all_evens(nums):
    evenNums = []
    for num in nums:
        if num % 2 == 0:
            evenNums.append(num)
    
    return evenNums

def get_odd_indices(items):
    result = []
    for i in range(len(items)):
        if i % 2!= 0:
            result.append(items[i])

    return result


def print_as_numbered_list(items):
    for i in range(1, len(items)):
        print(f'{i}. {items[i]}')
     


def get_range(start, stop):
    nums = []
    for num in range(start,stop):
        nums.append(num)
        
    return nums
    

def censor_vowels(word):
    chars = []
    for letter in word:
         if letter in "aeiou":
            chars.append("*")
         else:
            chars.append(letter)
    return "".join(chars)
            


def snake_to_camel(string):
    words = string.split("_")
    camel_case = []
    for word in words:
        camel_case.append(word.title())
    return "".join(camel_case)

#in the for loop we are splitting into two words
# on line 109, implies the first letter and then you make that an uppercase



def longest_word_length(words):
    longest = len(words[0])
    
    for word in words:
        if longest < len(word):
            longest = len(word)

    return longest


def truncate(string):
    result  = []
    for i in range(len(string)):
        if len(result) == 0 or string[i] != result[len(result)-1]:
            result.append(string[i])

    return "".join(result)

# change to look at the letter versus indexing
# use enumerate


def has_balanced_parens(string):
    parens = 0
    for char in string:
        if char == '(':
            parens += 1
        elif char == ')':
            parens -= 1
        
    if parens != 0:
        return False
    else:
        return True




def compress(string):
    compressed = []
    
    curr_char = ""
    char_count=0
    for char in string:
        if char != curr_char:
            compressed.append(curr_char)

            if char_count > 1:
                compressed.append(str(char_count))
            curr_char = char
            char_count = 0

        char_count += 1
        
    compressed.append(curr_char)
    if char_count > 1:
        compressed.append(str(char_count))

    return "".join(compressed)





print(output_all_items(["Suji", "Megan"]))
print(get_all_evens([40,30,55,47,89,100]))
print(get_odd_indices(["Suji","Megan",55,47,89,100]))
print_as_numbered_list(["Suji","Megan",55,47,89,100])
print(get_range(0,5))
print(censor_vowels("hello world"))
print(snake_to_camel("hello_world"))
print(longest_word_length(["Suji","Megan","Ari"]))
print(truncate("aaaaaaaabcdeabcdeeeeee"))
print(has_balanced_parens("(help)"))
print(compress('aabbaabb'))

