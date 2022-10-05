# FizzBuzz is a game that has gained in popularity as a programming assignment to weed out non-programmers during job interviews. The object of the assignment is less about solving it correctly according to the below rules and more about showing the programmer understands basic, necessary tools such as if-/else-statements and loops. The rules of FizzBuzz are as follows:
#
# For numbers 1 through 100,
#
# if the number is divisible by 3 print Fizz;
# if the number is divisible by 5 print Buzz;
# if the number is divisible by 3 and 5 (15) print FizzBuzz;
# else, print the number.

#Name : Rohit SHines Date: =Sept 20th Comments: Pushing after 1st code Review
class Fizz1:
    def fizzBuzz(n=3):
        # ans list
        ans = []

        # Dictionary to store all fizzbuzz mappings
        fizz_buzz_dict = {3: "Fizz", 5: "Buzz"}

        # List of divisors which we will iterate over.
        divisors = [3, 5]

        for num in range(1, n + 1):

            num_ans_str = []

            for key in divisors:
                # If the num is divisible by key,
                # then add the corresponding string mapping to current num_ans_str
                if num % key == 0:
                    num_ans_str.append(fizz_buzz_dict[key])

            if not num_ans_str:
                num_ans_str.append(str(num))

            # Append the current answer str to the ans list
            ans.append(''.join(num_ans_str))

        print(ans)

obj=Fizz1
obj.fizzBuzz()