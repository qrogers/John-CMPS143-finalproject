from lxml import etree
import nltk
import re

class ADJP(etree.ElementBase):
    def getdescription(self):
        return 'Adjective Phrase'
class ADVP(etree.ElementBase):
    def getdescription(self):
        return 'Adverb Phrase'
class CD(etree.ElementBase):
    def getdescription(self):
        return 'Cardinal number'
class EX(etree.ElementBase):
    def getdescription(self):
        return 'Existential there'
class FRAG(etree.ElementBase):
    def getdescription(self):
        return 'Fragment'
class INTJ(etree.ElementBase):
    def getdescription(self):
        return 'Interjection.'
class S(etree.ElementBase): 
    def getdescription(self):
        return 'Simple declarative clase.'
class JJ(etree.ElementBase):
    def getdescription(self):
        return 'Adjective'
class JJR(etree.ElementBase):
    def getdescription(self):
        return 'Adjective, comparative.'
class JJS(etree.ElementBase):
    def getdescription(self):
        return 'Adjective, superlative.'
class VP(etree.ElementBase):
    def getdescription(self):
        return 'Verb Phrase.'
class LRB(etree.ElementBase):
    def getdescription(self):
        return 'Unknown'
class LS(etree.ElementBase):
    def getdescription(self):
        return 'List item marker'
class NP(etree.ElementBase):
    def getdescription(self):
        return 'Noun Phrase'
class NN(etree.ElementBase): 
    def getdescription(self):
        return 'Noun'
class NNP(etree.ElementBase):
    def getdescription(self):
        return 'Proper noun, singular'
class NNS(etree.ElementBase):
    def getdescription(self):
        return 'Noun,plural'
class NPTMP(etree.ElementBase):
    def getdescription(self):
        return 'Marks temporal or aspectual adverbials that answer the questions when.'
class MD(etree.ElementBase):
    def getdescription(self):
        return 'Modal'
class VBD(etree.ElementBase):
    def getdescription(self):
        return 'Verb, past tense'
class CC(etree.ElementBase):
    def getdescription(self):
        return 'Coordinating conjunction'
class VB(etree.ElementBase):
    def getdescription(self):
        return 'Verb, base form.'
class VBG(etree.ElementBase):
    def getdescription(self):
        return 'Verb, gerund or present participle.'
class IN(etree.ElementBase):
    def getdescription(self):
        return 'Proposition or subordinating conjunction.'
class DT(etree.ElementBase):
    def getdescription(self):
        return 'Determiner'
class PP(etree.ElementBase):
    def getdescription(self):
        return 'Prepositional Phrase'
class SBAR(etree.ElementBase):
    def getdescription(self):
        return 'Clause introduced by subordinating conjunction'
class PDT(etree.ElementBase):
    def getdescription(self):
        return 'Predeterminer'
class POS(etree.ElementBase):
    def getdescription(self):
        return'Posesive ending'
class PRP(etree.ElementBase):
    def getdescription(self):
        return 'Personal Pronoun'
class RB(etree.ElementBase):
    def getdescription(self):
        return 'Adverb'
class PRN(etree.ElementBase):
    def getdescription(self):
        return 'Parenthetical'
class RRB(etree.ElementBase):
    def getdescription(self):
        return 'unkown'
class PRT(etree.ElementBase):
    def getdescription(self):
        return 'Particle. Category for words that should be tagged RP'
class QP(etree.ElementBase):
    def getdescription(self):
        return 'Quantifier phrase'
class RP(etree.ElementBase):
    def getdescription(self):
        return 'Particle'
class SBARQ(etree.ElementBase):
    def getdescription(self):
        return 'Direct question introduced by wh-word or wh-phrase'
class SINV(etree.ElementBase):
    def getdescription(self):
        return 'Inverted declarative sentence'
class SQ(etree.ElementBase):
    def getdescription(self):
        return 'Inverted yes/no question.'
class TO(etree.ElementBase):
    def getdescription(self):
        return 'to'
class TMP(etree.ElementBase):
    def getdescription(self):
        return 'Marks temporal or aspectual adverbials that answer the question when, how, often, ore how long.'
class UCP(etree.ElementBase):
    def getdescription(self):
        return 'Unlike coordinated Phrase.'
class UH(etree.ElementBase):
    def getdescription(self):
        return 'Interjection'
class VBZ(etree.ElementBase):
    def getdescription(self):
        return 'Verb, 3rd person singular present'
class VBN(etree.ElementBase):
    def getdescription(self):
        return 'Verb, past participle'
class VBP(etree.ElementBase):
    def getdescription(self):
        return 'Verb, non-3rd person singular present'
class WHPP(etree.ElementBase):
    def getdescription(self):
        return 'Wh-prepositional Phrase.'
class WHADJP(etree.ElementBase):
    @property
    def match(self):
        return self.get('match')

    def getdescription(self):
        self.set('match', '[VP]')
        return 'WH-adverb phrase'
class WDT(etree.ElementBase):
    def getdescription(self):
        return 'Wh-determiner'
class WRB(etree.ElementBase):
    def getdescription(self):
        return 'wh-adverb'
class WP(etree.ElementBase):
    def getdescription(self):
        return 'wh-pronoun'
class WHADVP(etree.ElementBase):
    @property
    def match(self):
        return self.get('match')

    def getdescription(self):
        return 'wh-avdverb phrase'
class WHNP(etree.ElementBase):
    @property
    def match(self):
        return self.get('match')
    def getdescription(self):
        return 'Wh-noun Phrase. Introduces a clause with an NP gap.'
def getdescription(self):
        self.set('match', 'hello')
        return 'Wh-noun phrase.'
class X(etree.ElementBase):
    def getdescription(self):
        return 'Unkown, uncertain, unbracketable'

class ROOT(etree.ElementBase):
    def getdescription(self):
        return 'root'

class word(etree.ElementBase):
    @property
    def const(self):
        return self.get("const")
    
    @property
    def dep(self):
        return int(self.get("dep"))

    @property
    def mod(self):
        return int(self.get("dep"))

    @property
    def id(self):
        return self.get('id')

class doc(etree.ElementBase): pass


class GenerateXML:
    def __str__(self):
        return etree.tostring(self.tree.getroottree(), pretty_print=True, encoding='unicode')

    def __init__(self, dep_sents, par_sents):
        self.tree = doc()

        for par_sent, dep_sent in zip(par_sents, dep_sents):
            self._build(par_sent, dep_sent)

    def _build(self, par, dep, iters=[], index=0):
        if isinstance(par, nltk.tree.Tree) and re.search('\w+', par.label()) != None:
            elem = eval(par.label().replace('$', '').replace('-', ''))(description='')
            elem.set('description', elem.getdescription())
            self.tree.append(elem)
            self.tree = list(self.tree)[-1]
            it = iter(par)
            iters.append(it)
            return self._build(next(it), dep, iters=iters, index=index)
        else:
            if isinstance(par, str):
                try:
                    self.tree.append(word(par, id='word-' +str(index), 
                        const=self.tree.tag, 
                        dep=dep[index][2],
                        mod=dep[index][3],
                        ))
                    index = index + 1
                except:
                    print('error occured. Continuing...')
                    pass
            while iters: 
                n = next(iters[-1], None)
                if n:
                    return self._build(n, dep, iters=iters, index=index)
                iters.pop()
                self.tree = self.tree.getparent()
