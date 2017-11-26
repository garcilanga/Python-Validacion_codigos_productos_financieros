#!/usr/bin/env python
# -*- coding: utf-8 -*-
#encoding:utf-8

import pycountry
import random
import re

####################################################################################################
### Clase para validar y gestionar códigos CUSIP
### The Committee on Uniform Securities Identification Procedures number assigned by the CUSIP Service Bureau for U.S. and Canadian companies
### https://en.wikipedia.org/wiki/CUSIP
### https://www.rosettacode.org/wiki/CUSIP
### https://github.com/arthurdejong/python-stdnum/blob/master/stdnum/cusip.py
####################################################################################################

### Caracteres permitidos en un código CUSIP
CTT_CUSIP_CHARACTERS = u'0123456789ABCDEFGH JKLMN PQRSTUVWXYZ*@#'
CTT_CUSIP_CHARACTERS = re.sub('\s', '', CTT_CUSIP_CHARACTERS)

class CUSIP:

    ####################################################################################################
    ### Calcula el dígito de control de un código CUSIP
    ####################################################################################################
    def getChecksumCUSIP(self, body):
        if body:
            body = unicode(body).upper()
            if len(body) in (8, 9):
                body = body[:8]
                total = 0
                for i in range(8):
                    c = body[i]
                    if c.isdigit():
                        v = int(c)
                    elif c.isalpha():
                        p = ord(c) - ord('A') + 1
                        v = p + 9
                    elif c == '*':
                        v = 36
                    elif c == '@':
                        v = 37
                    elif c == '#':
                        v = 38
 
                    if i % 2 != 0:
                        v *= 2
 
                    total += int(v / 10) + v % 10
                return str((10 - (total % 10)) % 10)
        return None

    ####################################################################################################
    ### Determina si un código CUSIP es correcto (dígito de control)
    ####################################################################################################
    def isCUSIP(self, maybeCUSIP):
        return self.getOkCUSIP(maybeCUSIP) != ''

    ####################################################################################################
    ### Determina si un CUSIP es correcto. Retorna CUSIP o ''
    ####################################################################################################
    def getOkCUSIP(self, maybeCUSIP):
        if maybeCUSIP:
            maybeCUSIP = unicode(maybeCUSIP).upper()
            maybeCUSIP = re.sub('\s', '', maybeCUSIP)
            if len(maybeCUSIP) == 9:
                if all(x in CTT_CUSIP_CHARACTERS for x in maybeCUSIP):
                    if self.getChecksumCUSIP(maybeCUSIP[:-1]) == maybeCUSIP[-1]:
                        return maybeCUSIP
        return ''

    ####################################################################################################
    ### Genera un código CUSIP correcto (?)
    ####################################################################################################
    def createCUSIP(self):
        body = ''.join(map(lambda x: random.choice(list(CTT_CUSIP_CHARACTERS)), range(8)))
        control = self.getChecksumCUSIP(body)
        cusip = ''.join([body, control])
        return unicode(cusip)
    
if __name__ == "__main__":

    mgrcusip = CUSIP()
    cusip = mgrcusip.createCUSIP()
    
    print u'- CUSIP generado automáticamente                                    :', cusip
    print u'- El código %s ¿es un CUSIP válido?                          : %s' % (cusip, mgrcusip.isCUSIP(cusip))
    print u'- El código %s ¿es un CUSIP válido?                          : %s' % (cusip[:-1]+cusip[2], mgrcusip.isCUSIP(cusip[:-1]+cusip[2]))
    print u'- Devuelve %s si es un código CUSIP válido o nada si no lo es: %s' % (cusip, mgrcusip.getOkCUSIP(cusip))
    print u'- Devuelve %s si es un código CUSIP válido o nada si no lo es: %s' % (cusip[:-1]+cusip[2], mgrcusip.getOkCUSIP(cusip[:-1]+cusip[2]))
    print u'- Dígito de control de CUSIP para %s                         : %s' % (cusip, mgrcusip.getChecksumCUSIP(cusip))
    print u'- Dígito de control de CUSIP para %s                          : %s' % (cusip[:-1], mgrcusip.getChecksumCUSIP(cusip[:-1]))
    print u'- Dígito de control de CUSIP para %s                           : %s' % (cusip[:-2], mgrcusip.getChecksumCUSIP(cusip[:-2]))
    print u'- Dígito de control de CUSIP para %s                         : %s' % (cusip[:-1]+cusip[2], mgrcusip.getChecksumCUSIP(cusip[:-1]+cusip[2]))

