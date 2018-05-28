print('{0}, {1}, {2}'.format('a', 'b', 'c'))
print('{}, {}, {}'.format('a', 'b', 'c'))  # 3.1+ only
print('{2}, {1}, {0}'.format('a', 'b', 'c'))
print('{2}, {1}, {0}'.format(*'abc'))    # unpacking argument sequence
print('{0}{1}{0}'.format('abra', 'cad'))  # arguments' indices can be repeated

print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))
#'Coordinates: 37.24N, -115.81W'
coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print('Coordinates: {latitude}, {longitude}'.format(**coord))
#'Coordinates: 37.24N, -115.81W'

#Aligning the text and specifying a width:
print('{:<30}'.format('left aligned'))
#'left aligned                  '
print('{:>30}'.format('right aligned'))
#'                 right aligned'
print('{:^30}'.format('centered'))
#'           centered           '
print('{:*^30}'.format('centered'))  # use '*' as a fill char
#'***********centered***********'

#Replacing %+f, %-f, and % f and specifying a sign:
print('{:+f}; {:+f}'.format(3.14, -3.14))  # show it always
#'+3.140000; -3.140000'
print('{: f}; {: f}'.format(3.14, -3.14))  # show a space for positive numbers
#' 3.140000; -3.140000'
print('{:-f}; {:-f}'.format(3.14, -3.14))  # show only the minus -- same as '{:f}; {:f}'
#'3.140000; -3.140000'

#Replacing %x and %o and converting the value to different bases:
# format also supports binary numbers
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))
#'int: 42;  hex: 2a;  oct: 52;  bin: 101010'
# with 0x, 0o, or 0b as prefix:
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42))
#'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'

#Using the comma as a thousands separator:
print('{:,}'.format(1234567890))
#'1,234,567,890'

#Expressing a percentage:
points = 19
total = 22
print('Correct answers: {:.2%}'.format(points/total))
#'Correct answers: 86.36%'

#Using type-specific formatting:
import datetime
d = datetime.datetime(2010, 7, 4, 12, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))
#'2010-07-04 12:15:58'