# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 04:50:05 2020

@author: yoelr
"""
import thermosteam as tmo
import doctest

def test_stream_docs():
    doctest.testmod(tmo._stream)
    
def test_multi_stream_docs():
    doctest.testmod(tmo._multi_stream)
    
def test_chemicals_docs():
    doctest.testmod(tmo._chemicals)
    
def test_chemical_docs():
    doctest.testmod(tmo._chemical)
    
def test_reaction_docs():
    doctest.testmod(tmo.reaction._reaction)
    
def test_equilibrium_docs():
    doctest.testmod(tmo.equilibrium.bubble_point)
    doctest.testmod(tmo.equilibrium.dew_point)
    doctest.testmod(tmo.equilibrium.vle)
    doctest.testmod(tmo.equilibrium.lle)
    
    
def test_thermosteam():
    test_stream_docs()
    test_multi_stream_docs()
    test_chemicals_docs()
    test_chemical_docs()
    test_reaction_docs()
    test_equilibrium_docs()
    
if __name__ == '__main__':
    test_thermosteam()