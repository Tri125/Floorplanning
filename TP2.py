#!/usr/bin/env python
# encoding: utf-8
"""
TP2.py

Coéquipiers :
"""

import unittest




def main(objets):
    
    arbres = []
    
    #TODO
    
    return arbres





class TP2Tests(unittest.TestCase):
    def setUp(self):
        self.objets = []
        self.arbres = []
            
    def test1(self):
        self.objets = []
        self.objets.append(("A", 2, 7))
        self.objets.append(("B", 5, 3))
        self.arbres = []
        self.arbres.append('10:(-,A,B):35')
        self.arbres.append('10:(-,B,A):35')
        self.arbres.append('01:(|,A,B):35')
        self.arbres.append('01:(|,B,A):35')
        self.arbresRetournes = main(self.objets)
        self.assertTrue(len(self.arbresRetournes) > 0)
        for i in self.arbresRetournes:
            self.assertTrue(i in self.arbres)
        
    def test2(self):
        self.objets = []
        self.objets.append(("A", 2, 13))
        self.objets.append(("B", 11, 3))
        self.objets.append(("C", 5, 7))
        self.arbres = []
        self.arbres.append('101:(|,(-,A,B),C):100')
        self.arbres.append('101:(|,(-,B,A),C):100')
        self.arbres.append('101:(|,C,(-,A,B)):100')
        self.arbres.append('101:(|,C,(-,B,A)):100')
        self.arbres.append('010:(-,(|,A,B),C):100')
        self.arbres.append('010:(-,(|,B,A),C):100')
        self.arbres.append('010:(-,C,(|,A,B)):100')
        self.arbres.append('010:(-,C,(|,B,A)):100')
        self.arbresRetournes = main(self.objets)
        self.assertTrue(len(self.arbresRetournes) > 0)
        for i in self.arbresRetournes:
            self.assertTrue(i in self.arbres)
        
    def test3(self):
        self.objets = []
        self.objets.append(("A", 1, 1))
        self.objets.append(("B", 2, 1))
        self.objets.append(("C", 1, 3))
        self.arbres = []
        self.arbres.append('110:(|,(-,A,B),C):6')
        self.arbres.append('110:(|,(-,B,A),C):6')
        self.arbres.append('110:(|,C,(-,A,B)):6')
        self.arbres.append('110:(|,C,(-,B,A)):6')
        self.arbres.append('101:(-,(|,A,B),C):6')
        self.arbres.append('101:(-,(|,B,A),C):6')
        self.arbres.append('101:(-,C,(|,A,B)):6')
        self.arbres.append('101:(-,C,(|,B,A)):6')
        self.arbres.append('010:(|,(-,A,B),C):6')
        self.arbres.append('010:(|,(-,B,A),C):6')
        self.arbres.append('010:(|,C,(-,A,B)):6')
        self.arbres.append('010:(|,C,(-,B,A)):6')
        self.arbres.append('001:(-,(|,A,B),C):6')
        self.arbres.append('001:(-,(|,B,A),C):6')
        self.arbres.append('001:(-,C,(|,A,B)):6')
        self.arbres.append('001:(-,C,(|,B,A)):6')
        self.arbresRetournes = main(self.objets)
        self.assertTrue(len(self.arbresRetournes) > 0)
        for i in self.arbresRetournes:
            self.assertTrue(i in self.arbres)
        
    def test4(self):
        self.objets = []
        self.objets.append(("A", 1, 1))
        self.objets.append(("B", 2, 1))
        self.objets.append(("C", 2, 3))
        self.arbres = []
        self.arbres.append('110:(|,(-,A,B),C):9')
        self.arbres.append('110:(|,(-,B,A),C):9')
        self.arbres.append('110:(|,C,(-,A,B)):9')
        self.arbres.append('110:(|,C,(-,B,A)):9')
        self.arbres.append('101:(-,(|,A,B),C):9')
        self.arbres.append('101:(-,(|,B,A),C):9')
        self.arbres.append('101:(-,C,(|,A,B)):9')
        self.arbres.append('101:(-,C,(|,B,A)):9')
        self.arbres.append('010:(|,(-,A,B),C):9')
        self.arbres.append('010:(|,(-,B,A),C):9')
        self.arbres.append('010:(|,C,(-,A,B)):9')
        self.arbres.append('010:(|,C,(-,B,A)):9')
        self.arbres.append('001:(-,(|,A,B),C):9')
        self.arbres.append('001:(-,(|,B,A),C):9')
        self.arbres.append('001:(-,C,(|,A,B)):9')
        self.arbres.append('001:(-,C,(|,B,A)):9')
        self.arbresRetournes = main(self.objets)
        self.assertTrue(len(self.arbresRetournes) > 0)
        for i in self.arbresRetournes:
            self.assertTrue(i in self.arbres)
        
    def test5(self):
        self.objets = []
        self.objets.append(("A", 1, 2))
        self.objets.append(("B", 3, 2))
        self.objets.append(("C", 3, 4))
        self.arbres = []
        self.arbres.append('110:(|,(-,A,B),C):20')
        self.arbres.append('110:(|,(-,B,A),C):20')
        self.arbres.append('110:(|,C,(-,A,B)):20')
        self.arbres.append('110:(|,C,(-,B,A)):20')
        self.arbres.append('001:(-,(|,A,B),C):20')
        self.arbres.append('001:(-,(|,B,A),C):20')
        self.arbres.append('001:(-,C,(|,A,B)):20')
        self.arbres.append('001:(-,C,(|,B,A)):20')
        self.arbresRetournes = main(self.objets)
        self.assertTrue(len(self.arbresRetournes) > 0)
        for i in self.arbresRetournes:
            self.assertTrue(i in self.arbres)
        
    def test6(self):
        self.objets = []
        self.objets.append(("A", 2, 19))
        self.objets.append(("B", 17, 3))
        self.objets.append(("C", 5, 13))
        self.objets.append(("D", 11, 7))
        self.arbres = []
        self.arbres.append('1010:(-,A,(|,(-,B,C),D)):280')
        self.arbres.append('1010:(-,A,(|,(-,C,B),D)):280')
        self.arbres.append('1010:(-,A,(|,D,(-,B,C))):280')
        self.arbres.append('1010:(-,A,(|,D,(-,C,B))):280')
        self.arbres.append('1010:(-,(|,(-,B,C),D),A):280')
        self.arbres.append('1010:(-,(|,(-,C,B),D),A):280')
        self.arbres.append('1010:(-,(|,D,(-,B,C)),A):280')
        self.arbres.append('1010:(-,(|,D,(-,C,B)),A):280')
        self.arbres.append('0101:(|,A,(-,(|,B,C),D)):280')
        self.arbres.append('0101:(|,A,(-,(|,C,B),D)):280')
        self.arbres.append('0101:(|,A,(-,D,(|,B,C))):280')
        self.arbres.append('0101:(|,A,(-,D,(|,C,B))):280')
        self.arbres.append('0101:(|,(-,(|,B,C),D),A):280')
        self.arbres.append('0101:(|,(-,(|,C,B),D),A):280')
        self.arbres.append('0101:(|,(-,D,(|,B,C)),A):280')
        self.arbres.append('0101:(|,(-,D,(|,C,B)),A):280')
        self.arbresRetournes = main(self.objets)
        self.assertTrue(len(self.arbresRetournes) > 0)
        for i in self.arbresRetournes:
            self.assertTrue(i in self.arbres)
        
    def test7(self):
        self.objets = []
        self.objets.append(("A", 1, 2))
        self.objets.append(("B", 2, 3))
        self.objets.append(("C", 3, 4))
        self.objets.append(("D", 4, 5))
        self.arbres = []
        self.arbres.append('1001:(-,(|,(-,A,B),C),D):40')
        self.arbres.append('1001:(-,(|,(-,B,A),C),D):40')
        self.arbres.append('1001:(-,(|,C,(-,A,B)),D):40')
        self.arbres.append('1001:(-,(|,C,(-,B,A)),D):40')
        self.arbres.append('1001:(-,D,(|,(-,A,B),C)):40')
        self.arbres.append('1001:(-,D,(|,(-,B,A),C)):40')
        self.arbres.append('1001:(-,D,(|,C,(-,A,B))):40')
        self.arbres.append('1001:(-,D,(|,C,(-,B,A))):40')
        self.arbres.append('0110:(|,(-,(|,A,B),C),D):40')
        self.arbres.append('0110:(|,(-,(|,B,A),C),D):40')
        self.arbres.append('0110:(|,(-,C,(|,A,B)),D):40')
        self.arbres.append('0110:(|,(-,C,(|,B,A)),D):40')
        self.arbres.append('0110:(|,D,(-,(|,A,B),C)):40')
        self.arbres.append('0110:(|,D,(-,(|,B,A),C)):40')
        self.arbres.append('0110:(|,D,(-,C,(|,A,B))):40')
        self.arbres.append('0110:(|,D,(-,C,(|,B,A))):40')
        self.arbresRetournes = main(self.objets)
        self.assertTrue(len(self.arbresRetournes) > 0)
        for i in self.arbresRetournes:
            self.assertTrue(i in self.arbres)
        
    def test8(self):
        self.objets = []
        self.objets.append(("A", 2, 29))
        self.objets.append(("B", 23, 3))
        self.objets.append(("C", 5, 19))
        self.objets.append(("D", 17, 7))
        self.objets.append(("E", 11, 13))
        self.arbres = []
        self.arbres.append('10101:(|,(-,A,(|,(-,B,C),D)),E):583')
        self.arbres.append('10101:(|,(-,A,(|,(-,C,B),D)),E):583')
        self.arbres.append('10101:(|,(-,A,(|,D,(-,B,C))),E):583')
        self.arbres.append('10101:(|,(-,A,(|,D,(-,C,B))),E):583')
        self.arbres.append('10101:(|,(-,(|,(-,B,C),D),A),E):583')
        self.arbres.append('10101:(|,(-,(|,(-,C,B),D),A),E):583')
        self.arbres.append('10101:(|,(-,(|,D,(-,B,C)),A),E):583')
        self.arbres.append('10101:(|,(-,(|,D,(-,C,B)),A),E):583')
        self.arbres.append('10101:(|,E,(-,A,(|,(-,B,C),D))):583')
        self.arbres.append('10101:(|,E,(-,A,(|,(-,C,B),D))):583')
        self.arbres.append('10101:(|,E,(-,A,(|,D,(-,B,C)))):583')
        self.arbres.append('10101:(|,E,(-,A,(|,D,(-,C,B)))):583')
        self.arbres.append('10101:(|,E,(-,(|,(-,B,C),D),A)):583')
        self.arbres.append('10101:(|,E,(-,(|,(-,C,B),D),A)):583')
        self.arbres.append('10101:(|,E,(-,(|,D,(-,B,C)),A)):583')
        self.arbres.append('10101:(|,E,(-,(|,D,(-,C,B)),A)):583')
        self.arbres.append('01010:(-,(|,A,(-,(|,B,C),D)),E):583')
        self.arbres.append('01010:(-,(|,A,(-,(|,C,B),D)),E):583')
        self.arbres.append('01010:(-,(|,A,(-,D,(|,B,C))),E):583')
        self.arbres.append('01010:(-,(|,A,(-,D,(|,C,B))),E):583')
        self.arbres.append('01010:(-,(|,(-,(|,B,C),D),A),E):583')
        self.arbres.append('01010:(-,(|,(-,(|,C,B),D),A),E):583')
        self.arbres.append('01010:(-,(|,(-,D,(|,B,C)),A),E):583')
        self.arbres.append('01010:(-,(|,(-,D,(|,C,B)),A),E):583')
        self.arbres.append('01010:(-,E,(|,A,(-,(|,B,C),D))):583')
        self.arbres.append('01010:(-,E,(|,A,(-,(|,C,B),D))):583')
        self.arbres.append('01010:(-,E,(|,A,(-,D,(|,B,C)))):583')
        self.arbres.append('01010:(-,E,(|,A,(-,D,(|,C,B)))):583')
        self.arbres.append('01010:(-,E,(|,(-,(|,B,C),D),A)):583')
        self.arbres.append('01010:(-,E,(|,(-,(|,C,B),D),A)):583')
        self.arbres.append('01010:(-,E,(|,(-,D,(|,B,C)),A)):583')
        self.arbres.append('01010:(-,E,(|,(-,D,(|,C,B)),A)):583')
        self.arbresRetournes = main(self.objets)
        self.assertTrue(len(self.arbresRetournes) > 0)
        for i in self.arbresRetournes:
            self.assertTrue(i in self.arbres)
        
    def test9(self):
        self.objets = []
        self.objets.append(("A", 2, 37))
        self.objets.append(("B", 31, 3))
        self.objets.append(("C", 5, 29))
        self.objets.append(("D", 23, 7))
        self.objets.append(("E", 11, 19))
        self.objets.append(("F", 17, 13))
        self.arbres = []
        self.arbres.append('101010:(-,(|,(-,A,(|,D,E)),F),(|,B,C)):1080')
        self.arbres.append('101010:(-,(|,(-,A,(|,D,E)),F),(|,C,B)):1080')
        self.arbres.append('101010:(-,(|,(-,A,(|,E,D)),F),(|,B,C)):1080')
        self.arbres.append('101010:(-,(|,(-,A,(|,E,D)),F),(|,C,B)):1080')
        self.arbres.append('101010:(-,(|,B,C),(|,(-,A,(|,D,E)),F)):1080')
        self.arbres.append('101010:(-,(|,B,C),(|,(-,A,(|,E,D)),F)):1080')
        self.arbres.append('101010:(-,(|,B,C),(|,(-,(|,D,E),A),F)):1080')
        self.arbres.append('101010:(-,(|,B,C),(|,(-,(|,E,D),A),F)):1080')
        self.arbres.append('101010:(-,(|,B,C),(|,F,(-,A,(|,D,E)))):1080')
        self.arbres.append('101010:(-,(|,B,C),(|,F,(-,A,(|,E,D)))):1080')
        self.arbres.append('101010:(-,(|,B,C),(|,F,(-,(|,D,E),A))):1080')
        self.arbres.append('101010:(-,(|,B,C),(|,F,(-,(|,E,D),A))):1080')
        self.arbres.append('101010:(-,(|,C,B),(|,(-,A,(|,D,E)),F)):1080')
        self.arbres.append('101010:(-,(|,C,B),(|,(-,A,(|,E,D)),F)):1080')
        self.arbres.append('101010:(-,(|,C,B),(|,(-,(|,D,E),A),F)):1080')
        self.arbres.append('101010:(-,(|,C,B),(|,(-,(|,E,D),A),F)):1080')
        self.arbres.append('101010:(-,(|,C,B),(|,F,(-,A,(|,D,E)))):1080')
        self.arbres.append('101010:(-,(|,C,B),(|,F,(-,A,(|,E,D)))):1080')
        self.arbres.append('101010:(-,(|,C,B),(|,F,(-,(|,D,E),A))):1080')
        self.arbres.append('101010:(-,(|,C,B),(|,F,(-,(|,E,D),A))):1080')
        self.arbres.append('101010:(-,(|,(-,(|,D,E),A),F),(|,B,C)):1080')
        self.arbres.append('101010:(-,(|,(-,(|,D,E),A),F),(|,C,B)):1080')
        self.arbres.append('101010:(-,(|,(-,(|,E,D),A),F),(|,B,C)):1080')
        self.arbres.append('101010:(-,(|,(-,(|,E,D),A),F),(|,C,B)):1080')
        self.arbres.append('101010:(-,(|,F,(-,A,(|,D,E))),(|,B,C)):1080')
        self.arbres.append('101010:(-,(|,F,(-,A,(|,D,E))),(|,C,B)):1080')
        self.arbres.append('101010:(-,(|,F,(-,A,(|,E,D))),(|,B,C)):1080')
        self.arbres.append('101010:(-,(|,F,(-,A,(|,E,D))),(|,C,B)):1080')
        self.arbres.append('101010:(-,(|,F,(-,(|,D,E),A)),(|,B,C)):1080')
        self.arbres.append('101010:(-,(|,F,(-,(|,D,E),A)),(|,C,B)):1080')
        self.arbres.append('101010:(-,(|,F,(-,(|,E,D),A)),(|,B,C)):1080')
        self.arbres.append('101010:(-,(|,F,(-,(|,E,D),A)),(|,C,B)):1080')
        self.arbres.append('010101:(|,(-,(|,A,(-,D,E)),F),(-,B,C)):1080')
        self.arbres.append('010101:(|,(-,(|,A,(-,D,E)),F),(-,C,B)):1080')
        self.arbres.append('010101:(|,(-,(|,A,(-,E,D)),F),(-,B,C)):1080')
        self.arbres.append('010101:(|,(-,(|,A,(-,E,D)),F),(-,C,B)):1080')
        self.arbres.append('010101:(|,(-,B,C),(-,(|,A,(-,D,E)),F)):1080')
        self.arbres.append('010101:(|,(-,B,C),(-,(|,A,(-,E,D)),F)):1080')
        self.arbres.append('010101:(|,(-,B,C),(-,(|,(-,D,E),A),F)):1080')
        self.arbres.append('010101:(|,(-,B,C),(-,(|,(-,E,D),A),F)):1080')
        self.arbres.append('010101:(|,(-,B,C),(-,F,(|,A,(-,D,E)))):1080')
        self.arbres.append('010101:(|,(-,B,C),(-,F,(|,A,(-,E,D)))):1080')
        self.arbres.append('010101:(|,(-,B,C),(-,F,(|,(-,D,E),A))):1080')
        self.arbres.append('010101:(|,(-,B,C),(-,F,(|,(-,E,D),A))):1080')
        self.arbres.append('010101:(|,(-,C,B),(-,(|,A,(-,D,E)),F)):1080')
        self.arbres.append('010101:(|,(-,C,B),(-,(|,A,(-,E,D)),F)):1080')
        self.arbres.append('010101:(|,(-,C,B),(-,(|,(-,D,E),A),F)):1080')
        self.arbres.append('010101:(|,(-,C,B),(-,(|,(-,E,D),A),F)):1080')
        self.arbres.append('010101:(|,(-,C,B),(-,F,(|,A,(-,D,E)))):1080')
        self.arbres.append('010101:(|,(-,C,B),(-,F,(|,A,(-,E,D)))):1080')
        self.arbres.append('010101:(|,(-,C,B),(-,F,(|,(-,D,E),A))):1080')
        self.arbres.append('010101:(|,(-,C,B),(-,F,(|,(-,E,D),A))):1080')
        self.arbres.append('010101:(|,(-,(|,(-,D,E),A),F),(-,B,C)):1080')
        self.arbres.append('010101:(|,(-,(|,(-,D,E),A),F),(-,C,B)):1080')
        self.arbres.append('010101:(|,(-,(|,(-,E,D),A),F),(-,B,C)):1080')
        self.arbres.append('010101:(|,(-,(|,(-,E,D),A),F),(-,C,B)):1080')
        self.arbres.append('010101:(|,(-,F,(|,A,(-,D,E))),(-,B,C)):1080')
        self.arbres.append('010101:(|,(-,F,(|,A,(-,D,E))),(-,C,B)):1080')
        self.arbres.append('010101:(|,(-,F,(|,A,(-,E,D))),(-,B,C)):1080')
        self.arbres.append('010101:(|,(-,F,(|,A,(-,E,D))),(-,C,B)):1080')
        self.arbres.append('010101:(|,(-,F,(|,(-,D,E),A)),(-,B,C)):1080')
        self.arbres.append('010101:(|,(-,F,(|,(-,D,E),A)),(-,C,B)):1080')
        self.arbres.append('010101:(|,(-,F,(|,(-,E,D),A)),(-,B,C)):1080')
        self.arbres.append('010101:(|,(-,F,(|,(-,E,D),A)),(-,C,B)):1080')
        self.arbresRetournes = main(self.objets)
        self.assertTrue(len(self.arbresRetournes) > 0)
        for i in self.arbresRetournes:
            self.assertTrue(i in self.arbres)
        
    


if __name__ == '__main__':
    
    
    unittest.main()
    
    
    
    
    
    
    
    
    
    
    