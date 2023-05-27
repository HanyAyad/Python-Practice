def donuts(count):
return


def both_ends(s):
return


def fix_start(s):
return


def mix_up(a, b):
return


def test(got, expected):
if got == expected:
prefix = ' OK '
else:
prefix = '  X '
print('{p} got: {g}; expected: {e}'.format(p=prefix, g=got, e=expected))


def main():
print('donuts')
test(donuts(4), 'Number of donuts: 4')
test(donuts(9), 'Number of donuts: 9')
test(donuts(10), 'Number of donuts: many')
test(donuts(99), 'Number of donuts: many')

print()
print('both_ends')
test(both_ends('spring'), 'spng')
test(both_ends('Hello'), 'Helo')
test(both_ends('a'), '')
test(both_ends('xyz'), 'xyyz')

print()
print('fix_start')
test(fix_start('babble'), 'ba**le')
test(fix_start('aardvark'), 'a*rdv*rk')
test(fix_start('google'), 'goo*le')
test(fix_start('donut'), 'donut')

print()
print('mix_up')
test(mix_up('mix', 'pod'), 'pox mid')
test(mix_up('dog', 'dinner'), 'dig donner')
test(mix_up('gnash', 'sport'), 'spash gnort')
test(mix_up('pezzy', 'firm'), 'fizzy perm')


if __name__ == '__main__':
main()
