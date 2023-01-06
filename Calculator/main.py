from calculator import *
from To_Repeat_Again import *
from convert_into_final_number import *
test=True
while True:
    if test==True:
        call=calculator()
        convert(call)
        test=takechoice()
    else:
        print("""==================================
 Thank you for using my calculator
==================================""" )
        break
