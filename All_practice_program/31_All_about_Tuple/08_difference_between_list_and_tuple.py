
'''
List and Tuple are exactly same except small difference:
List objects are mutable where as Tuple objects are immutable.
 
 In both cases insertion order is preserved, duplicate objects are allowed, heterogenous
objects are allowed, index and slicing are supported. 


List :
1) List is a Group of Comma separeated Values within Square Brackets and Square Brackets are mandatory.
Eg: i = [10, 20, 30, 40]

2) List Objects are Mutable i.e. once we creates List Object we can perform any changes in that Object.
Eg: i[1] = 70

3) If the Content is not fixed and keep on changing then we should go for List.

4) List Objects can not used as Keys for Dictionries because Keys should be Hashable and Immutable.


Tuple :
1) Tuple is a Group of Comma separeated Values within Parenthesis and Parenthesis are optional.
Eg: t = (10, 20, 30, 40)
    t = 10, 20, 30, 40 

2) Tuple Objeccts are Immutable i.e. once we creates Tuple Object we cannot change its content.
t[1] = 70  ValueError: tuple object does not support item assignment.

3) If the content is fixed and never changes then we should go for Tuple.

4) Tuple Objects can be used as Keys for Dictionries because Keys should be Hashable and Immutable.
'''
