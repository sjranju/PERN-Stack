inp = input("Hey! Can you see this?, Yes or No \n")
print('You said', inp)

txt = input('Please enter a number: ')

try:
    num = int(txt)
    print('The number you have entered is', num)
except ValueError:
    print("You haven't entered a number, it's either string or text")
    
salary = 4400
text = "You make {}$ a year"
print(text.format(salary))

string = 'Bob likes to play {act} and has {1} kids and {0} siblings'
print(string.format(3, 6, act='chess'))

print('Bob likes to play {game} and eats {0} with {1}'.format('pizza', 'muddipalya', game='Football'))