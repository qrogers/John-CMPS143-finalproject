from lxml import etree
from nlpxml import *
import nltk
from nltk.tree import *
import re
import os


class Reader():
    def __iter__(self):
        return iter(self.texts)

    def __init__(self, basedir):
        files = sorted(os.listdir(basedir),
                key=lambda filename: int(re.search(r'(?<=-)\d{2}(?=\.)', filename).group(0) ))

        blogs = []
        fables = []

        for i in range(0, len(files), 20):
            batch = sorted(files[i:i+20])
            blog = batch[0:10]
            fable = batch[10:20]

            fables.append(self._getdict(fable, basedir))
            blogs.append(self._getdict(blog, basedir))

        self.texts =  fables + blogs
    def _getdict(self, files, basedir):
        return  {
            'answers': self._getanswers(open(basedir + files[0]).read()),
            'questions': self._getquestions(open(basedir + files[0]).read()),
            'types': self._gettypes(open(basedir + files[0]).read()),
            'q_dep': self._getqdep(open(basedir + files[2]).read()),
            'q_par': self._getqpar(open(basedir + files[3]).read()),
            'sch_dep': self._getschdep(open(basedir + files[5]).read()),
            'sch_par': self._getschpar(open(basedir + files[6]).read()),
            'story_dep': self._getstorydep(open(basedir + files[8]).read()),
            'story_par': self._getstorypar(open(basedir + files[9]).read())
        }

    def _getanswers(self, text):
        return re.findall('(?<=Answer: ).+(?=\\n)', text)

    def _getquestions(self, text):
        return re.findall('(?<=Question: ).+(?=\\n)', text)

    def _gettypes(self, text):
        return re.findall('(?<=Type: ).+(?=\\n)', text)

    def _getqdep(self, text):
        return  [[items.split('\t') for items in sent.split('\n')[1:]]
            for sent in text.split('\n\n')[:-1]]

    def _getqpar(self, text):
        return [Tree.fromstring(sent) 
                for sent in re.findall('\(ROOT.+(?=\\n)', text)]

    def _getschdep(self, text):
        return [[items.split('\t') for items in sent.split('\n')]
            for sent in text.split('\n\n')[:-1]]

    def _getschpar(self, text):
        return [Tree.fromstring(sent) for sent in text.split('\n')[:-1]]

    def _getstorydep(self, text):
        return [[items.split('\t') for items in sent.split('\n')]
            for sent in text.split('\n\n')[:-1]]

    def _getstorypar(self, text):
        return [Tree.fromstring(sent) for sent in text.split('\n')[:-1]]

if __name__ == "__main__":
    texts = Reader('datasets/')

    for i, DOC in enumerate(texts, 1):
        filenames = [('sch_par', 'sch_dep'), 
                     ('story_par', 'story_dep'),
                     ('q_par', 'q_dep')]
        for par, dep in filenames:
            open('XML/' + str(i) + "_" +  par.split('_')[0], 'w').write(str(GenerateXML(DOC[dep], DOC[par])))
