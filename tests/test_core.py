import pytest
import sys, os
# This block is not neccessary if you instaled your package
# using e.g. pip install -e
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), # location of this file
            os.pardir, # and one level up, in linux ../
        )
    )
)
# EOBlock

import playground

def test_find_peaks():
    peaks = playground.core.find_peaks([0, 2, 1])
    assert peaks == [2]  # erwartet wird ein Element, das soll 2 sein
    
def test_find_two_peaks():
    peaks = playground.core.find_peaks([0, 2, 1, 0, 2, 1])
    assert peaks == [2, 2]  
    
def test_find_peaks_max_edge():
    peaks = playground.core.find_peaks([2, 1, 1])
    assert peaks == [2]  
    
def test_find_peaks_empty():
    peaks = playground.core.find_peaks([])
    assert peaks == [] 
    
def test_find_peaks_colors():
    peaks = playground.core.find_peaks([(1,2,3), (0,0,1), (7,8,9)])
    assert peaks == [(0,0,1)]
    
def test_find_peaks_colors_two_peaks():
    peaks = playground.core.find_peaks([(1,2,3), (0,0,1), (7,8,9), (0,1,1), (50,60,4)])
    assert peaks == [(0,0,1), (0,1,1)]
