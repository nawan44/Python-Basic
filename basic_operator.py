#compare
a = 4
b = 7

#more than
res = b > 9
print(b, '>', '=', res  )
res = a > 9
print(a, '>', '=', res  )
res = b > 6
print(b, '>', '=', res  )
res = a > 3
print(a, '>', '=', res  )

#Less than
res = a < 3
print(a, '<', '=', res  )
res = b < 3
print(b, '<', '=', res  )
res = a < 10
print(a, '<', '=', res  )
res = b < 10
print(b, '<', '=', res  )

#more than equal to
res = b > 7
print(b, '>=', '=', res  )
res = a > 7
print(a, '>=', '=', res  )
res = b >= 7
print(b, '>=', '=', res  )
res = a >= 3
print(a, '>=', '=', res  )

#less than equal to
res = a <= 4
print(a, '<=', '=', res  )
res = b <= 4
print(b, '<=', '=', res  )
res = a <= 10
print(a, '<=', '=', res  )
res = b <= 10
print(b, '<=', '=', res  )

# compare ==
res = a == 4
print(a, '==', '=', res  )
res = b == 4
print(b, '==', '=', res  )

#not equal to
res = a != 4
print(a, '!=', '=', res  )
res = b != 4
print(b, '!=', '=', res  )


#object_oriented_programming identitiy

x = 4
y = 3
print('value x =', x,', id = ' , hex(id(x)))
print('value y =', y,', id = ' , hex(id(y)))
resu = x is y
print ('x is y =', resu)