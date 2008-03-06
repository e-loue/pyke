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


# family.daughter_of(daughter, father, mother)
# family.son_of(son, father, mother)

def init(engine):
    def daughter_of(daughter, father, mother):
        engine.add_universal_fact('family', 'daughter_of',
                                            (daughter, father, mother))
    def son_of(son, father, mother):
        engine.add_universal_fact('family', 'son_of', (son, father, mother))

    son_of('arthur2', 'arthur1', 'bertha_o')
    daughter_of('helen', 'arthur1', 'bertha_o')
    daughter_of('roberta', 'arthur1', 'bertha_o')

    daughter_of('gladis', 'john', 'bertha_c')
    daughter_of('sarah_r', 'john', 'bertha_c')
    daughter_of('alice', 'marshall1', 'bertha_c')
    son_of('edmond', 'marshall1', 'bertha_c')
    daughter_of('kathleen', 'marshall1', 'bertha_c')
    daughter_of('darleen', 'marshall1', 'bertha_c')
    daughter_of('birdie', 'marshall1', 'bertha_c')
    son_of('marshall2', 'marshall1', 'bertha_c')

    daughter_of('donna', 'david_r', 'sarah_r')
    son_of('david_r2', 'david_r', 'sarah_r')
    daughter_of('shirley', 'david_r', 'sarah_r')

    daughter_of('sarah_a', 'val', 'donna')

    daughter_of('heidi_m', 'brian', 'shirley')
    daughter_of('holly', 'brian', 'shirley')

    daughter_of('anne', 'chuck', 'alice')
    daughter_of('carol', 'chuck', 'alice')

    son_of('matt', 'ralph', 'anne')

    daughter_of('nanette', 'arthur2', 'kathleen')
    son_of('arthur3', 'arthur2', 'kathleen')
    daughter_of('sue', 'arthur2', 'kathleen')
    son_of('ed', 'arthur2', 'kathleen')
    daughter_of('marilyn', 'arthur2', 'kathleen')
    son_of('david_b', 'arthur2', 'kathleen')
    daughter_of('m_helen', 'arthur2', 'kathleen')

    daughter_of('beverly', 'michael_b', 'nanette')
    daughter_of('dianna', 'michael_b', 'nanette')
    daughter_of('teresa', 'michael_b', 'nanette')
    son_of('nick', 'paul', 'nanette')
    daughter_of('katrina', 'paul', 'nanette')

    son_of('albert2', 'albert1', 'dianna')
    son_of('jack', 'albert1', 'dianna')
    daughter_of('samantha', 'mike_g', 'dianna')

    daughter_of('tiffany', 'chad', 'teresa')
    son_of('tyler', 'chad', 'teresa')

    daughter_of('anita', 'arthur3', 'julie')
    son_of('justin', 'arthur3', 'julie')
    son_of('brian_d', 'arthur3', 'julie')
    daughter_of('debbie', 'arthur3', 'julie')
    son_of('arthur4', 'arthur3', 'lisa')
    daughter_of('rachael', 'arthur3', 'lisa')

    daughter_of('heidi_j', 'steve', 'sue')
    daughter_of('sarah_k', 'al', 'sue')

    daughter_of('dominique', 'arthur_x', 'heidi_j')

    son_of('jacob', 'frankie', 'sarah_k')
    son_of('justin_m', 'gary', 'sarah_k')

    son_of('keith', 'ed', 'ann')
    daughter_of('barbara', 'ed', 'ann')
    son_of('ramon', 'ed', 'ann')
    daughter_of('mary_k', 'ed', 'michelle')

    son_of('m_thomas', 'bruce', 'marilyn')
    son_of('david_a', 'bruce', 'marilyn')

    daughter_of('jackie', 'david_b', 'colleen')
    son_of('corey', 'david_b', 'colleen')
    daughter_of('andrea', 'david_b', 'colleen')

    son_of('alex', 'greg', 'jackie')

    daughter_of('amanda', 'michael_k', 'm_helen')
    daughter_of('tammy', 'michael_k', 'm_helen')
    daughter_of('crystal', 'michael_k', 'm_helen')

    daughter_of('joyce', 'frederik', 'mary')
    daughter_of('phyllis', 'frederik', 'mary')
    son_of('thomas', 'frederik', 'mary')

    son_of('david_c', 'chris', 'joyce')
    daughter_of('dee', 'chris', 'joyce')
    son_of('danny', 'chris', 'joyce')

    daughter_of('norma', 'allen', 'ismay')
    son_of('john_w', 'allen', 'ismay')
    son_of('bill', 'allen', 'ismay')
    son_of('chuck_w', 'allen', 'ismay')

    daughter_of('jonni', 'john_w', 'cleo')
    daughter_of('lorri', 'john_w', 'cleo')
    son_of('mitch', 'john_w', 'cleo')

    daughter_of('charli', 'joseph', 'jonni')

    son_of('steve_w', 'bill', 'elvina')
    son_of('jim', 'bill', 'elvina')
    daughter_of('jeri', 'bill', 'elvina')
    daughter_of('annette', 'bill', 'elvina')
    daughter_of('helen_w', 'bill', 'elvina')
    daughter_of('mary_w', 'bill', 'elvina')

    daughter_of('jamie', 'jim', 'sandy_w')
    son_of('jimjim', 'jim', 'sandy_w')
    son_of('johnjohn', 'jim', 'sandy_w')

    son_of('david_w', 'bob', 'annette')
    daughter_of('jessica', 'bob', 'annette')
    daughter_of('bridget', 'bob', 'annette')

    daughter_of('victoria', 'brian_w', 'helen_w')
    son_of('brian2', 'brian_w', 'helen_w')

    son_of('bruce', 'thomas', 'norma')
    son_of('fred_a', 'thomas', 'norma')
    son_of('tim', 'thomas', 'norma')
    daughter_of('vicki', 'thomas', 'norma')
    daughter_of('jill', 'thomas', 'norma')

