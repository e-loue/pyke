# $Id$
# coding=utf-8
#
# Copyright © 2007 Bruce Frederiksen
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from pyke import fact_base

family = fact_base.fact_base('family')

# example:
# family.add_universal_fact('daughter_of', ('gladis', 'john', 'bertha_c'))

# daughter_of(daughter, father, mother)
# son_of(son, father, mother)

family.add_universal_fact('son_of', ('arthur2', 'arthur1', 'bertha_o'))
family.add_universal_fact('daughter_of', ('helen', 'arthur1', 'bertha_o'))
family.add_universal_fact('daughter_of', ('roberta', 'arthur1', 'bertha_o'))

family.add_universal_fact('daughter_of', ('gladis', 'john', 'bertha_c'))
family.add_universal_fact('daughter_of', ('sarah_r', 'john', 'bertha_c'))
family.add_universal_fact('daughter_of', ('alice', 'marshall1', 'bertha_c'))
family.add_universal_fact('son_of', ('edmond', 'marshall1', 'bertha_c'))
family.add_universal_fact('daughter_of', ('kathleen', 'marshall1', 'bertha_c'))
family.add_universal_fact('daughter_of', ('darleen', 'marshall1', 'bertha_c'))
family.add_universal_fact('daughter_of', ('birdie', 'marshall1', 'bertha_c'))
family.add_universal_fact('son_of', ('marshall2', 'marshall1', 'bertha_c'))

family.add_universal_fact('daughter_of', ('donna', 'david_r', 'sarah_r'))
family.add_universal_fact('son_of', ('david_r2', 'david_r', 'sarah_r'))
family.add_universal_fact('daughter_of', ('shirley', 'david_r', 'sarah_r'))

family.add_universal_fact('daughter_of', ('sarah_a', 'val', 'donna'))

family.add_universal_fact('daughter_of', ('heidi_m', 'brian', 'shirley'))
family.add_universal_fact('daughter_of', ('holly', 'brian', 'shirley'))

family.add_universal_fact('daughter_of', ('anne', 'chuck', 'alice'))
family.add_universal_fact('daughter_of', ('carol', 'chuck', 'alice'))

family.add_universal_fact('son_of', ('matt', 'ralph', 'anne'))

family.add_universal_fact('daughter_of', ('nanette', 'arthur2', 'kathleen'))
family.add_universal_fact('son_of', ('arthur3', 'arthur2', 'kathleen'))
family.add_universal_fact('daughter_of', ('sue', 'arthur2', 'kathleen'))
family.add_universal_fact('son_of', ('ed', 'arthur2', 'kathleen'))
family.add_universal_fact('daughter_of', ('marilyn', 'arthur2', 'kathleen'))
family.add_universal_fact('son_of', ('david_b', 'arthur2', 'kathleen'))
family.add_universal_fact('daughter_of', ('m_helen', 'arthur2', 'kathleen'))

family.add_universal_fact('daughter_of', ('beverly', 'michael_b', 'nanette'))
family.add_universal_fact('daughter_of', ('dianna', 'michael_b', 'nanette'))
family.add_universal_fact('daughter_of', ('teresa', 'michael_b', 'nanette'))
family.add_universal_fact('son_of', ('nick', 'paul', 'nanette'))
family.add_universal_fact('daughter_of', ('katrina', 'paul', 'nanette'))

family.add_universal_fact('son_of', ('albert2', 'albert1', 'dianna'))
family.add_universal_fact('son_of', ('jack', 'albert1', 'dianna'))
family.add_universal_fact('daughter_of', ('samantha', 'mike_g', 'dianna'))

family.add_universal_fact('daughter_of', ('tiffany', 'chad', 'teresa'))
family.add_universal_fact('son_of', ('tyler', 'chad', 'teresa'))

family.add_universal_fact('daughter_of', ('anita', 'arthur3', 'julie'))
family.add_universal_fact('son_of', ('justin', 'arthur3', 'julie'))
family.add_universal_fact('son_of', ('brian_d', 'arthur3', 'julie'))
family.add_universal_fact('daughter_of', ('debbie', 'arthur3', 'julie'))
family.add_universal_fact('son_of', ('arthur4', 'arthur3', 'lisa'))
family.add_universal_fact('daughter_of', ('rachael', 'arthur3', 'lisa'))

family.add_universal_fact('daughter_of', ('heidi_j', 'steve', 'sue'))
family.add_universal_fact('daughter_of', ('sarah_k', 'al', 'sue'))

family.add_universal_fact('daughter_of', ('dominique', 'arthur_x', 'heidi_j'))

family.add_universal_fact('son_of', ('jacob', 'frankie', 'sarah_k'))
family.add_universal_fact('son_of', ('justin_m', 'gary', 'sarah_k'))

family.add_universal_fact('son_of', ('keith', 'ed', 'ann'))
family.add_universal_fact('daughter_of', ('barbara', 'ed', 'ann'))
family.add_universal_fact('son_of', ('ramon', 'ed', 'ann'))
family.add_universal_fact('daughter_of', ('mary_k', 'ed', 'michelle'))

family.add_universal_fact('son_of', ('m_thomas', 'bruce', 'marilyn'))
family.add_universal_fact('son_of', ('david_a', 'bruce', 'marilyn'))

family.add_universal_fact('daughter_of', ('jackie', 'david_b', 'colleen'))
family.add_universal_fact('son_of', ('corey', 'david_b', 'colleen'))
family.add_universal_fact('daughter_of', ('andrea', 'david_b', 'colleen'))

family.add_universal_fact('son_of', ('alex', 'greg', 'jackie'))

family.add_universal_fact('daughter_of', ('amanda', 'michael_k', 'm_helen'))
family.add_universal_fact('daughter_of', ('tammy', 'michael_k', 'm_helen'))
family.add_universal_fact('daughter_of', ('crystal', 'michael_k', 'm_helen'))


family.add_universal_fact('daughter_of', ('joyce', 'frederik', 'mary'))
family.add_universal_fact('daughter_of', ('phyllis', 'frederik', 'mary'))
family.add_universal_fact('son_of', ('thomas', 'frederik', 'mary'))

family.add_universal_fact('son_of', ('david_c', 'chris', 'joyce'))
family.add_universal_fact('daughter_of', ('dee', 'chris', 'joyce'))
family.add_universal_fact('son_of', ('danny', 'chris', 'joyce'))

family.add_universal_fact('daughter_of', ('norma', 'allen', 'ismay'))
family.add_universal_fact('son_of', ('john_w', 'allen', 'ismay'))
family.add_universal_fact('son_of', ('bill', 'allen', 'ismay'))
family.add_universal_fact('son_of', ('chuck_w', 'allen', 'ismay'))

family.add_universal_fact('daughter_of', ('jonni', 'john_w', 'cleo'))
family.add_universal_fact('daughter_of', ('lorri', 'john_w', 'cleo'))
family.add_universal_fact('son_of', ('mitch', 'john_w', 'cleo'))

family.add_universal_fact('daughter_of', ('charli', 'joseph', 'jonni'))

family.add_universal_fact('son_of', ('steve_w', 'bill', 'elvina'))
family.add_universal_fact('son_of', ('jim', 'bill', 'elvina'))
family.add_universal_fact('daughter_of', ('jeri', 'bill', 'elvina'))
family.add_universal_fact('daughter_of', ('annette', 'bill', 'elvina'))
family.add_universal_fact('daughter_of', ('helen_w', 'bill', 'elvina'))
family.add_universal_fact('daughter_of', ('mary_w', 'bill', 'elvina'))

family.add_universal_fact('daughter_of', ('jamie', 'jim', 'sandy_w'))
family.add_universal_fact('son_of', ('jimjim', 'jim', 'sandy_w'))
family.add_universal_fact('son_of', ('johnjohn', 'jim', 'sandy_w'))

family.add_universal_fact('son_of', ('david_w', 'bob', 'annette'))
family.add_universal_fact('daughter_of', ('jessica', 'bob', 'annette'))
family.add_universal_fact('daughter_of', ('bridget', 'bob', 'annette'))

family.add_universal_fact('daughter_of', ('victoria', 'brian_w', 'helen_w'))
family.add_universal_fact('son_of', ('brian2', 'brian_w', 'helen_w'))

family.add_universal_fact('son_of', ('bruce', 'thomas', 'norma'))
family.add_universal_fact('son_of', ('fred_a', 'thomas', 'norma'))
family.add_universal_fact('son_of', ('tim', 'thomas', 'norma'))
family.add_universal_fact('daughter_of', ('vicki', 'thomas', 'norma'))
family.add_universal_fact('daughter_of', ('jill', 'thomas', 'norma'))

