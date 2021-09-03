# x= '[abc]' either a or b or c
# x= '^[abc]'except abc
# x= '[a-z]' a to z
# x= '[A-Z]' A to Z
# x= '[a-zA-Z]'both lower and upper case checked
# x= '[0-9]'   check digit
# x= '[^a-zA-Z0-9]' special symbols
# x= '\s' check space
# x= '\d' check digit
# x= '\D' Except digit
# x= '\w' all words except special characters
# x= '\W' for special characters



Quantifiers
# x='a+' a including group
# x='a*' count including zero number of a
# x='a?' count a as each including zero number of a
# x='a{2}' 2 number of position
# x='a{2,3}' minimum 2 a and maximum 3 a
# x='^a' checking starting with a
# x='$a' check ending with a