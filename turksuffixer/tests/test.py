# -*- encoding: utf-8 -*-
import unittest
import re
import io
from pkg_resources import resource_string
from turksuffixer import Suffixer as Suffix

class ValueTest(unittest.TestCase):
    def setUp(self):
        self.simplewords = []
        self.numbers     = []
        self.exceptions  = []
        self.consonant   = []
        self.possesive   = []
        self.others      = []
        test_list = [('simplewords',self.simplewords),
                     ('numbers'    ,self.numbers    ),
                     ('exceptions' ,self.exceptions ),
                     ('consonantharmony',self.consonant),
                     ('possesive', self.possesive),
                     ('others',    self.others)
                     ]
        self.possessive_content = resource_string("turksuffixer", "sozluk/iyelik.txt")
        for filename,namelist in test_list:
            with io.open('tests/' + filename,'r',encoding='utf8') as infile:
                for line in [x for x in infile if not x.strip().startswith('#')]:
                    #result = re.findall(r'(\w+ )={}', line, re.UNICODE)
                    if len(line.strip()) == 0: continue
                    name, suffixes = line.split('=')
                    suffixes = suffixes.strip()[1:-1].split(',')
                    namelist.append((name.strip(), suffixes))
    def test_simplewords(self):
        self.basetest(self.simplewords)
    def test_numbers(self):
        self.basetest(self.numbers)
    def test_exceptions(self):
        self.basetest(self.exceptions)
    def test_consonant(self):
        self.basetest(self.consonant)
    def test_possesive(self):
        self.basetest(self.possesive)
    def test_others(self):
        self.basetest(self.others)
    def basetest(self, namelist):
        suffix = ['H','A','DA','DAn']
        ekle = Suffix()
        for name, suffixes in namelist:
            for sf, correctsf in zip(suffix,suffixes):
                rt = ekle.getSuffix(name,sf)
                self.assertEqual(correctsf.strip(), rt, u"'{}' için '{}' dönmesi gerekirken '{}' döndü.".format(name,correctsf,rt).encode('utf8'))
    def tearDown(self):
        file("sozluk/iyelik.txt","w").write(self.possessive_content);
        
        
if __name__ == '__main__':
    unittest.main()
