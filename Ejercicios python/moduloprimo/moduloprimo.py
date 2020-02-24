#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Santiago
#
# Created:     24/02/2020
# Copyright:   (c) Santiago 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#
def primo(numero):
    if numero<1:
        return "no es primo"
    elif numero==2:
        return "es primo"
    else:
        for i in range (2,numero):
            if numero % i == 0:
                return "no es primo"
            else:
                return "es primo"