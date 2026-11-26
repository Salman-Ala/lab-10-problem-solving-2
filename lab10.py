# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
# Outline 
#make an empty list for my stack
#go through each token one at a time
#if the token is a number turn it into an int and add it to the stack
#if the token is an operator take the top two numbers off the stack
#the first number I take off is b and the second one is a
#this is important for subtraction and division
#do the math using a and b then put the answer back on the stack
#after going through all the tokens the number left on the stack is my answer
    stack = []

    for token in tokens:
        if token == "+":
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif token == "-":
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        elif token == "*":
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        elif token == "/":
            b = stack.pop()
            a = stack.pop()
            stack.append(int(a / b))
        else:
            stack.append(int(token))

    return stack[0]


def decode_string(s):
    # Outline:
#make two empty stacks. One for the strings and one for the numbers
#keep track of the current string and number while going through s
#if I see a number add it to the current number
#if I see "[" save the string and number in the stacks
#then reset them so I can start fresh inside the brackets
#if I see "]" take the last string and number out of the stacks
# repeat the current string using that number and add it to the saved string
#if I see a letter add it to the current string
#after going through everything the current string is my final answer
   string_stack = []
   number_stack = []
   current_string = ""
   current_number = 0

   for ch in s:
        if ch.isdigit():
            
            current_number = current_number * 10 + int(ch)
        elif ch == "[":
            string_stack.append(current_string)
            number_stack.append(current_number)
            current_string = ""
            current_number = 0
        elif ch == "]":
            old_string = string_stack.pop()
            times = number_stack.pop()
            current_string = old_string + current_string * times
        else:
            
            current_string = current_string + ch

   return current_string


def daily_temperatures(temps):
    # Outline:
#make an empty list called answer to save my results
#go through each day one at a time and call it today
#set days_to_wait = 0 for each day in case I don't find a warmer day
#check all the days after today one by one
#if I find a day that is warmer than today figure out how many days away it is
#add that number and stop looking using break
#add days_to_wait to my answer list
#once I check all the days return the answer list
    answer = []

    for today in range(len(temps)):
        days_to_wait = 0   
      
        for later_day in range(today + 1, len(temps)):
            if temps[later_day] > temps[today]:
             
                days_to_wait = later_day - today
                break     

        answer.append(days_to_wait)

    return answer

def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: `grid` is a list of equal-length strings of "1" (land) and "0" (water).
    #   Count the islands - groups of "1"s connected up/down/left/right (not diagonally).
    #   Example: ["11000","11000","00100","00011"]  ->  3
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    # print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    pass


if __name__ == "__main__":
    main()
