#!/usr/bin/env python
# encoding: utf-8
"""
TP2.py

"""

import unittest
import TP2


def main(objets):
    
    return TP2.main(objets)







class TP2Tests(unittest.TestCase):
    print()
    print("TESTING")
    def setUp(self):
        self.objets = []
        self.arbres = []
            
    def test1(self):
        self.objets = []
        self.objets.append(("A", 2, 997))
        self.objets.append(("B", 503, 499))
        self.arbres = []
        self.arbres.append('10:(-,A,B):499497')
        self.arbres.append('10:(-,B,A):499497')
        self.arbres.append('01:(|,A,B):499497')
        self.arbres.append('01:(|,B,A):499497')
        self.arbresRetournes = main(self.objets)
        
        print()
        if len(self.arbresRetournes) > 0:
        	tous = True
        	au_moins_un = False
        	for i in self.arbresRetournes:
        		if i in self.arbres:
        			au_moins_un = True
        		else:
        			tous = False
        	if tous:
        		print("test1 : 5 points")
        	elif au_moins_un:
        		print("test1 (au moins 1 arbre valide)")
        		print("premier arbre valide :")
        		print(self.arbres[0])
        		print("arbres retournés :")
        		for i in self.arbresRetournes:
        			if i in self.arbres:
        				print(i + ' VALIDE')
        			else:
        				print(i + ' NON VALIDE')
        	else:
        		print("test1 (aucun arbre valide)")
        		print("premier arbre valide :")
        		print(self.arbres[0])
        		print("arbres retournés :")
        		for i in self.arbresRetournes:
        			if i in self.arbres:
        				print(i + ' VALIDE')
        			else:
        				print(i + ' NON VALIDE')
        else:
        	print("test1 : 0 point")
        
        """
        self.assertTrue(len(self.arbresRetournes) > 0)
        for i in self.arbresRetournes:
            self.assertTrue(i in self.arbres)
        """
        
    def test2(self):
        self.objets = []
        self.objets.append(("A", 3, 991))
        self.objets.append(("B", 509, 491))
        self.objets.append(("C", 983, 5))
        self.arbres = []
        self.arbres.append('100:(|,(-,A,C),B):736500')
        self.arbres.append('100:(|,B,(-,A,C)):736500')
        self.arbres.append('100:(|,B,(-,C,A)):736500')
        self.arbres.append('100:(|,(-,C,A),B):736500')
        self.arbres.append('011:(-,(|,A,C),B):736500')
        self.arbres.append('011:(-,B,(|,A,C)):736500')
        self.arbres.append('011:(-,B,(|,C,A)):736500')
        self.arbres.append('011:(-,(|,C,A),B):736500')
        self.arbresRetournes = main(self.objets)
        
        print()
        if len(self.arbresRetournes) > 0:
        	tous = True
        	au_moins_un = False
        	for i in self.arbresRetournes:
        		if i in self.arbres:
        			au_moins_un = True
        		else:
        			tous = False
        	if tous:
        		print("test2 : 5 points")
        	elif au_moins_un:
        		print("test2 (au moins 1 arbre valide)")
        		print("premier arbre valide :")
        		print(self.arbres[0])
        		print("arbres retournés :")
        		for i in self.arbresRetournes:
        			if i in self.arbres:
        				print(i + ' VALIDE')
        			else:
        				print(i + ' NON VALIDE')
        	else:
        		print("test2 (aucun arbre valide)")
        		print("premier arbre valide :")
        		print(self.arbres[0])
        		print("arbres retournés :")
        		for i in self.arbresRetournes:
        			if i in self.arbres:
        				print(i + ' VALIDE')
        			else:
        				print(i + ' NON VALIDE')
        else:
        	print("test2 : 0 point")
        
    def test3(self):
        self.objets = []
        self.objets.append(("A", 7, 977))
        self.objets.append(("B", 521, 487))
        self.objets.append(("C", 971, 11))
        self.objets.append(("D", 479, 523))
        self.arbres = []
        self.arbres.append('1001:(-,A,(|,B,(-,C,D))):741524')
        self.arbres.append('1001:(-,A,(|,B,(-,D,C))):741524')
        self.arbres.append('1001:(-,A,(|,(-,C,D),B)):741524')
        self.arbres.append('1001:(-,A,(|,(-,D,C),B)):741524')
        self.arbres.append('1001:(-,(|,B,(-,C,D)),A):741524')
        self.arbres.append('1001:(-,(|,B,(-,D,C)),A):741524')
        self.arbres.append('1001:(-,(|,(-,C,D),B),A):741524')
        self.arbres.append('1001:(-,(|,(-,D,C),B),A):741524')
        self.arbres.append('0110:(|,A,(-,B,(|,C,D))):741524')
        self.arbres.append('0110:(|,A,(-,B,(|,D,C))):741524')
        self.arbres.append('0110:(|,A,(-,(|,C,D),B)):741524')
        self.arbres.append('0110:(|,A,(-,(|,D,C),B)):741524')
        self.arbres.append('0110:(|,(-,B,(|,C,D)),A):741524')
        self.arbres.append('0110:(|,(-,B,(|,D,C)),A):741524')
        self.arbres.append('0110:(|,(-,(|,C,D),B),A):741524')
        self.arbres.append('0110:(|,(-,(|,D,C),B),A):741524')
        self.arbresRetournes = main(self.objets)
        
        print()
        if len(self.arbresRetournes) > 0:
        	tous = True
        	au_moins_un = False
        	for i in self.arbresRetournes:
        		if i in self.arbres:
        			au_moins_un = True
        		else:
        			tous = False
        	if tous:
        		print("test3 : 5 points")
        	elif au_moins_un:
        		print("test3 (au moins 1 arbre valide)")
        		print("premier arbre valide :")
        		print(self.arbres[0])
        		print("arbres retournés :")
        		for i in self.arbresRetournes:
        			if i in self.arbres:
        				print(i + ' VALIDE')
        			else:
        				print(i + ' NON VALIDE')
        	else:
        		print("test3 (aucun arbre valide)")
        		print("premier arbre valide :")
        		print(self.arbres[0])
        		print("arbres retournés :")
        		for i in self.arbresRetournes:
        			if i in self.arbres:
        				print(i + ' VALIDE')
        			else:
        				print(i + ' NON VALIDE')
        else:
        	print("test3 : 0 point")
        
    def test4(self):
        self.objets = []
        self.objets.append(("A", 13, 967))
        self.objets.append(("B", 541, 467))
        self.objets.append(("C", 953, 17))
        self.objets.append(("D", 463, 547))
        self.objets.append(("E", 251, 241))
        self.arbres = []
        self.arbres.append('10011:(-,A,(|,(-,(|,B,D),C),E)):660513')
        self.arbres.append('10011:(-,(|,(-,A,(|,B,D)),E),C):660513')
        self.arbres.append('10011:(-,A,(|,(-,C,(|,B,D)),E)):660513')
        self.arbres.append('10011:(-,A,(|,(-,C,(|,D,B)),E)):660513')
        self.arbres.append('10011:(-,A,(|,(-,(|,D,B),C),E)):660513')
        self.arbres.append('10011:(-,(|,(-,A,(|,D,B)),E),C):660513')
        self.arbres.append('10011:(-,A,(|,E,(-,(|,B,D),C))):660513')
        self.arbres.append('10011:(-,A,(|,E,(-,C,(|,B,D)))):660513')
        self.arbres.append('10011:(-,A,(|,E,(-,C,(|,D,B)))):660513')
        self.arbres.append('10011:(-,A,(|,E,(-,(|,D,B),C))):660513')
        self.arbres.append('10011:(-,(|,(-,(|,B,D),A),E),C):660513')
        self.arbres.append('10011:(-,(|,(-,(|,B,D),C),E),A):660513')
        self.arbres.append('10011:(-,C,(|,(-,A,(|,B,D)),E)):660513')
        self.arbres.append('10011:(-,C,(|,(-,A,(|,D,B)),E)):660513')
        self.arbres.append('10011:(-,C,(|,(-,(|,B,D),A),E)):660513')
        self.arbres.append('10011:(-,(|,(-,C,(|,B,D)),E),A):660513')
        self.arbres.append('10011:(-,C,(|,(-,(|,D,B),A),E)):660513')
        self.arbres.append('10011:(-,(|,(-,C,(|,D,B)),E),A):660513')
        self.arbres.append('10011:(-,C,(|,E,(-,A,(|,B,D)))):660513')
        self.arbres.append('10011:(-,C,(|,E,(-,A,(|,D,B)))):660513')
        self.arbres.append('10011:(-,C,(|,E,(-,(|,B,D),A))):660513')
        self.arbres.append('10011:(-,C,(|,E,(-,(|,D,B),A))):660513')
        self.arbres.append('10011:(-,(|,(-,(|,D,B),A),E),C):660513')
        self.arbres.append('10011:(-,(|,(-,(|,D,B),C),E),A):660513')
        self.arbres.append('10011:(-,(|,E,(-,A,(|,B,D))),C):660513')
        self.arbres.append('10011:(-,(|,E,(-,A,(|,D,B))),C):660513')
        self.arbres.append('10011:(-,(|,E,(-,(|,B,D),A)),C):660513')
        self.arbres.append('10011:(-,(|,E,(-,(|,B,D),C)),A):660513')
        self.arbres.append('10011:(-,(|,E,(-,C,(|,B,D))),A):660513')
        self.arbres.append('10011:(-,(|,E,(-,C,(|,D,B))),A):660513')
        self.arbres.append('10011:(-,(|,E,(-,(|,D,B),A)),C):660513')
        self.arbres.append('10011:(-,(|,E,(-,(|,D,B),C)),A):660513')
        self.arbres.append('01100:(|,A,(-,(|,(-,B,D),C),E)):660513')
        self.arbres.append('01100:(|,(-,(|,A,(-,B,D)),E),C):660513')
        self.arbres.append('01100:(|,A,(-,(|,C,(-,B,D)),E)):660513')
        self.arbres.append('01100:(|,A,(-,(|,C,(-,D,B)),E)):660513')
        self.arbres.append('01100:(|,A,(-,(|,(-,D,B),C),E)):660513')
        self.arbres.append('01100:(|,(-,(|,A,(-,D,B)),E),C):660513')
        self.arbres.append('01100:(|,A,(-,E,(|,(-,B,D),C))):660513')
        self.arbres.append('01100:(|,A,(-,E,(|,C,(-,B,D)))):660513')
        self.arbres.append('01100:(|,A,(-,E,(|,C,(-,D,B)))):660513')
        self.arbres.append('01100:(|,A,(-,E,(|,(-,D,B),C))):660513')
        self.arbres.append('01100:(|,(-,(|,(-,B,D),A),E),C):660513')
        self.arbres.append('01100:(|,(-,(|,(-,B,D),C),E),A):660513')
        self.arbres.append('01100:(|,C,(-,(|,A,(-,B,D)),E)):660513')
        self.arbres.append('01100:(|,C,(-,(|,A,(-,D,B)),E)):660513')
        self.arbres.append('01100:(|,C,(-,(|,(-,B,D),A),E)):660513')
        self.arbres.append('01100:(|,(-,(|,C,(-,B,D)),E),A):660513')
        self.arbres.append('01100:(|,C,(-,(|,(-,D,B),A),E)):660513')
        self.arbres.append('01100:(|,(-,(|,C,(-,D,B)),E),A):660513')
        self.arbres.append('01100:(|,C,(-,E,(|,A,(-,B,D)))):660513')
        self.arbres.append('01100:(|,C,(-,E,(|,A,(-,D,B)))):660513')
        self.arbres.append('01100:(|,C,(-,E,(|,(-,B,D),A))):660513')
        self.arbres.append('01100:(|,C,(-,E,(|,(-,D,B),A))):660513')
        self.arbres.append('01100:(|,(-,(|,(-,D,B),A),E),C):660513')
        self.arbres.append('01100:(|,(-,(|,(-,D,B),C),E),A):660513')
        self.arbres.append('01100:(|,(-,E,(|,A,(-,B,D))),C):660513')
        self.arbres.append('01100:(|,(-,E,(|,A,(-,D,B))),C):660513')
        self.arbres.append('01100:(|,(-,E,(|,(-,B,D),A)),C):660513')
        self.arbres.append('01100:(|,(-,E,(|,(-,B,D),C)),A):660513')
        self.arbres.append('01100:(|,(-,E,(|,C,(-,B,D))),A):660513')
        self.arbres.append('01100:(|,(-,E,(|,C,(-,D,B))),A):660513')
        self.arbres.append('01100:(|,(-,E,(|,(-,D,B),A)),C):660513')
        self.arbres.append('01100:(|,(-,E,(|,(-,D,B),C)),A):660513')
        self.arbresRetournes = main(self.objets)
        
        print()
        if len(self.arbresRetournes) > 0:
        	tous = True
        	au_moins_un = False
        	for i in self.arbresRetournes:
        		if i in self.arbres:
        			au_moins_un = True
        		else:
        			tous = False
        	if tous:
        		print("test4 : 5 points")
        	elif au_moins_un:
        		print("test4 (au moins 1 arbre valide)")
        		print("premier arbre valide :")
        		print(self.arbres[0])
        		print("arbres retournés :")
        		for i in self.arbresRetournes:
        			if i in self.arbres:
        				print(i + ' VALIDE')
        			else:
        				print(i + ' NON VALIDE')
        	else:
        		print("test4 (aucun arbre valide)")
        		print("premier arbre valide :")
        		print(self.arbres[0])
        		print("arbres retournés :")
        		for i in self.arbresRetournes:
        			if i in self.arbres:
        				print(i + ' VALIDE')
        			else:
        				print(i + ' NON VALIDE')
        else:
        	print("test4 : 0 point")
        
    def test5(self):
        self.objets = []
        self.objets.append(("A", 19, 947))
        self.objets.append(("B", 557, 461))
        self.objets.append(("C", 941, 23))
        self.objets.append(("D", 457, 563))
        self.objets.append(("E", 257, 239))
        self.objets.append(("F", 743, 751))
        self.arbres = []
        self.arbres.append('101101:(|,(-,A,(|,(-,B,D),(-,E,F))),C):1338337')
        self.arbres.append('101101:(|,(-,A,(|,(-,B,D),(-,F,E))),C):1338337')
        self.arbres.append('101101:(|,(-,A,(|,(-,D,B),(-,E,F))),C):1338337')
        self.arbres.append('101101:(|,(-,A,(|,(-,D,B),(-,F,E))),C):1338337')
        self.arbres.append('101101:(|,(-,A,(|,(-,E,F),(-,B,D))),C):1338337')
        self.arbres.append('101101:(|,(-,A,(|,(-,E,F),(-,D,B))),C):1338337')
        self.arbres.append('101101:(|,(-,A,(|,(-,F,E),(-,B,D))),C):1338337')
        self.arbres.append('101101:(|,(-,A,(|,(-,F,E),(-,D,B))),C):1338337')
        self.arbres.append('101101:(|,(-,(|,(-,B,D),(-,E,F)),A),C):1338337')
        self.arbres.append('101101:(|,(-,(|,(-,B,D),(-,F,E)),A),C):1338337')
        self.arbres.append('101101:(|,C,(-,A,(|,(-,B,D),(-,E,F)))):1338337')
        self.arbres.append('101101:(|,C,(-,A,(|,(-,B,D),(-,F,E)))):1338337')
        self.arbres.append('101101:(|,C,(-,A,(|,(-,D,B),(-,E,F)))):1338337')
        self.arbres.append('101101:(|,C,(-,A,(|,(-,D,B),(-,F,E)))):1338337')
        self.arbres.append('101101:(|,C,(-,A,(|,(-,E,F),(-,B,D)))):1338337')
        self.arbres.append('101101:(|,C,(-,A,(|,(-,E,F),(-,D,B)))):1338337')
        self.arbres.append('101101:(|,C,(-,A,(|,(-,F,E),(-,B,D)))):1338337')
        self.arbres.append('101101:(|,C,(-,A,(|,(-,F,E),(-,D,B)))):1338337')
        self.arbres.append('101101:(|,C,(-,(|,(-,B,D),(-,E,F)),A)):1338337')
        self.arbres.append('101101:(|,C,(-,(|,(-,B,D),(-,F,E)),A)):1338337')
        self.arbres.append('101101:(|,C,(-,(|,(-,D,B),(-,E,F)),A)):1338337')
        self.arbres.append('101101:(|,C,(-,(|,(-,D,B),(-,F,E)),A)):1338337')
        self.arbres.append('101101:(|,C,(-,(|,(-,E,F),(-,B,D)),A)):1338337')
        self.arbres.append('101101:(|,C,(-,(|,(-,E,F),(-,D,B)),A)):1338337')
        self.arbres.append('101101:(|,C,(-,(|,(-,F,E),(-,B,D)),A)):1338337')
        self.arbres.append('101101:(|,C,(-,(|,(-,F,E),(-,D,B)),A)):1338337')
        self.arbres.append('101101:(|,(-,(|,(-,D,B),(-,E,F)),A),C):1338337')
        self.arbres.append('101101:(|,(-,(|,(-,D,B),(-,F,E)),A),C):1338337')
        self.arbres.append('101101:(|,(-,(|,(-,E,F),(-,B,D)),A),C):1338337')
        self.arbres.append('101101:(|,(-,(|,(-,E,F),(-,D,B)),A),C):1338337')
        self.arbres.append('101101:(|,(-,(|,(-,F,E),(-,B,D)),A),C):1338337')
        self.arbres.append('101101:(|,(-,(|,(-,F,E),(-,D,B)),A),C):1338337')
        self.arbres.append('010010:(-,(|,A,(-,(|,B,D),(|,E,F))),C):1338337')
        self.arbres.append('010010:(-,(|,A,(-,(|,B,D),(|,F,E))),C):1338337')
        self.arbres.append('010010:(-,(|,A,(-,(|,D,B),(|,E,F))),C):1338337')
        self.arbres.append('010010:(-,(|,A,(-,(|,D,B),(|,F,E))),C):1338337')
        self.arbres.append('010010:(-,(|,A,(-,(|,E,F),(|,B,D))),C):1338337')
        self.arbres.append('010010:(-,(|,A,(-,(|,E,F),(|,D,B))),C):1338337')
        self.arbres.append('010010:(-,(|,A,(-,(|,F,E),(|,B,D))),C):1338337')
        self.arbres.append('010010:(-,(|,A,(-,(|,F,E),(|,D,B))),C):1338337')
        self.arbres.append('010010:(-,(|,(-,(|,B,D),(|,E,F)),A),C):1338337')
        self.arbres.append('010010:(-,(|,(-,(|,B,D),(|,F,E)),A),C):1338337')
        self.arbres.append('010010:(-,C,(|,A,(-,(|,B,D),(|,E,F)))):1338337')
        self.arbres.append('010010:(-,C,(|,A,(-,(|,B,D),(|,F,E)))):1338337')
        self.arbres.append('010010:(-,C,(|,A,(-,(|,D,B),(|,E,F)))):1338337')
        self.arbres.append('010010:(-,C,(|,A,(-,(|,D,B),(|,F,E)))):1338337')
        self.arbres.append('010010:(-,C,(|,A,(-,(|,E,F),(|,B,D)))):1338337')
        self.arbres.append('010010:(-,C,(|,A,(-,(|,E,F),(|,D,B)))):1338337')
        self.arbres.append('010010:(-,C,(|,A,(-,(|,F,E),(|,B,D)))):1338337')
        self.arbres.append('010010:(-,C,(|,A,(-,(|,F,E),(|,D,B)))):1338337')
        self.arbres.append('010010:(-,C,(|,(-,(|,B,D),(|,E,F)),A)):1338337')
        self.arbres.append('010010:(-,C,(|,(-,(|,B,D),(|,F,E)),A)):1338337')
        self.arbres.append('010010:(-,C,(|,(-,(|,D,B),(|,E,F)),A)):1338337')
        self.arbres.append('010010:(-,C,(|,(-,(|,D,B),(|,F,E)),A)):1338337')
        self.arbres.append('010010:(-,C,(|,(-,(|,E,F),(|,B,D)),A)):1338337')
        self.arbres.append('010010:(-,C,(|,(-,(|,E,F),(|,D,B)),A)):1338337')
        self.arbres.append('010010:(-,C,(|,(-,(|,F,E),(|,B,D)),A)):1338337')
        self.arbres.append('010010:(-,C,(|,(-,(|,F,E),(|,D,B)),A)):1338337')
        self.arbres.append('010010:(-,(|,(-,(|,D,B),(|,E,F)),A),C):1338337')
        self.arbres.append('010010:(-,(|,(-,(|,D,B),(|,F,E)),A),C):1338337')
        self.arbres.append('010010:(-,(|,(-,(|,E,F),(|,B,D)),A),C):1338337')
        self.arbres.append('010010:(-,(|,(-,(|,E,F),(|,D,B)),A),C):1338337')
        self.arbres.append('010010:(-,(|,(-,(|,F,E),(|,B,D)),A),C):1338337')
        self.arbres.append('010010:(-,(|,(-,(|,F,E),(|,D,B)),A),C):1338337')
        self.arbresRetournes = main(self.objets)
        
        print()
        if len(self.arbresRetournes) > 0:
        	tous = True
        	au_moins_un = False
        	for i in self.arbresRetournes:
        		if i in self.arbres:
        			au_moins_un = True
        		else:
        			tous = False
        	if tous:
        		print("test5 : 5 points")
        	elif au_moins_un:
        		print("test5 (au moins 1 arbre valide)")
        		print("premier arbre valide :")
        		print(self.arbres[0])
        		print("arbres retournés :")
        		for i in self.arbresRetournes:
        			if i in self.arbres:
        				print(i + ' VALIDE')
        			else:
        				print(i + ' NON VALIDE')
        	else:
        		print("test5 (aucun arbre valide)")
        		print("premier arbre valide :")
        		print(self.arbres[0])
        		print("arbres retournés :")
        		for i in self.arbresRetournes:
        			if i in self.arbres:
        				print(i + ' VALIDE')
        			else:
        				print(i + ' NON VALIDE')
        else:
        	print("test5 : 0 point")
        
    


if __name__ == '__main__':
    
    unittest.main()
    
    
    
    
    
    
    
    
    
    
    