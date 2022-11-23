# Hi, I'm code kudos, this program prints a stylised monthly calendar using python, termcolor & pyfiglet
## Hope you like it
### To see more like this Subscribe to 
#### Youtube: @codekudos
##### Instagram: @codekudos
###### Twitter: @code_kudos

from termcolor import colored
from pyfiglet import Figlet
import calendar

cal = calendar.month(2022,11)

f = Figlet(font='digital')
print(colored(f.renderText(cal),'green'))