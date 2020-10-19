# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 23:54:35 2020

@author: Administrator
"""

# use xml.sax parse dblp.xml. Give each author an ID and put them in a file.
# find collaboration relations of all authors and output them to a file. One relation's format is like (id1,id2)

# we first extract all author(s) in the same paper, then update the dict of authors, after which we extract
# collaboration relation(s) in this paper
import xml.sax
from xml.sax.handler import feature_external_ges

paper_tags = ('article', 'inproceedings', 'proceedings', 'book', 'incollection', 'phdthesis', 'mastersthesis', 'www')

# class authorHandler(xml.sax.ContentHandler):  # extract all authors

    # def __init__(self):
    #     self.CurrentData = ""  # tag's name
    #     self.dict = {}  # save all authors. The key is an author's name, the value is his id
    #     self.name = ""  # the name of an author
    #     self.id = 0  # the ID of an author
    #     self.contents = []
    #     self.author = []  # all authors for the same paper
    #     self.year = ""  # the year of publication


    # def resolveEntity(self, publicID, systemID):
    #     print("authorHandler.resolveEntity(): %s %s" % (publicID, systemID))
    #     return systemID

    # def startElement(self, tag, attributes):
    #     if tag != None and len(tag.strip()) > 0:
    #         self.CurrentData = tag

    # def endElement(self, tag):
    #     if tag != None and len(tag.strip()) > 0:
    #         if tag in paper_tags:
    #             if len(self.author) > 0 and self.year != '2015':
    #             #if self.CurrentData == 'author':  # this tag is author, save it in the dict
    #                 for authorname in self.author:
    #                     exist = self.dict.get(authorname, -1)
    #                     if exist == -1:  # if this author have not been added into dict
    #                         self.dict[authorname] = self.id
    #                         self.id = self.id + 1
    #
    #             self.author.clear()
    #         elif self.CurrentData == 'author':
    #             self.author.append(self.name)
    #             self.contents.clear()

    # def characters(self, content):
    #     if content != '\n':
    #         if self.CurrentData == 'author':
    #             self.contents.append(content)
    #             self.name = ''.join(self.contents)
    #         # self.name += content.strip()
    #         elif self.CurrentData == "year":
    #             self.year = content.strip()


class collabrationHandler(xml.sax.ContentHandler):  # extract all collaboration relations
    def __init__(self, file):
        self.CurrentData = ""  # tag's name
        self.dict = {}  # save all authors. The key is an author's name, the value is his id
        self.name = ""  # the name of an author
        self.id = 0  # the ID of an author
        self.paper = False  # if the tag is in paper_tags, paper = True
        self.author = []  # all authors for the same paper
        self.file = file  # Output collaboration relation to file
        self.edge = set()  # Edge's set
        self.contents = []  # all authors for the same paper
        self.year = ""  # the year of publication
        self.author_id = [] # all authors' id in one publication

    def resolveEntity(self, publicID, systemID):
        print("collabrationHandler.resolveEntity(): %s %s" % (publicID, systemID))
        return systemID

    def startElement(self, tag, attributes):
        if tag != None and len(tag.strip()) > 0:
            self.CurrentData = tag
            if tag in paper_tags:
            #if tag == 'article' or tag == 'inproceeding':
                self.author_id.clear()  # start processing a new paper, old collaboration need to be deleted
                self.paper = True

    def characters(self, content):
        if self.paper == True and content != '\n':
            if self.CurrentData == 'author':
                self.contents.append(content)
                self.name = ''.join(self.contents)

            elif self.CurrentData == "year":
                self.year = content.strip()
            #self.name = content

    def endElement(self, tag):

        if tag != None and len(tag.strip()) > 0:
            if tag in paper_tags:
                if len(self.author) > 0 and self.year != '2015':
                #if self.CurrentData == 'author':  # this tag is author, save it in the dict
                    # update the dict of authors
                    for authorname in self.author:
                        exist = self.dict.get(authorname, -1)
                        if exist == -1:  # if this author have not been added into dict
                            self.dict[authorname] = self.id
                            self.id = self.id + 1
                    # get the id of authors
                    for authorname1 in self.author:
                        self.author_id.append(self.dict[authorname1])  # add this author's id
                        # isAuthor = self.dict.get(authorname, -1)  # isAuthor == -1 means that this content is not an author's name
                        # if isAuthor != -1:
                        #     self.author_id.append(self.dict[self.name])  # add this author's id
                self.author.clear()
                self.paper = False
                for i in self.author_id:
                    for j in self.author_id:
                        if i < j and (i, j) not in self.edge:  # edge
                            self.file.write(str(i) + ' ' + str(j) + '\n')
                            self.edge.add((i, j))
            elif self.CurrentData == 'author':
                self.author.append(self.name)
                self.contents.clear()
        #if tag in paper_tags:
        #if (tag == 'article' or tag == 'inproceeding') and self.paper == True:  # One paper's tag close
"""
            self.paper = False
            for i in self.author:
                for j in self.author:
                    if i < j and (i, j) not in self.edge:  # edge
                        self.file.write(str(i) + ' ' + str(j) + '\n')
                        self.edge.add((i, j))
"""




# set xml parser
parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
parser.setFeature(feature_external_ges, True)
# handler1 = authorHandler()
# parser.setContentHandler(handler1)
# parser.setEntityResolver(handler1)
# parser.setDTDHandler(handler1)
# parser.parse('dblp.xml')




with open('collaboration.txt', 'w') as f:
    handler = collabrationHandler(f)
    parser.setContentHandler(handler)
    parser.setEntityResolver(handler)
    parser.setDTDHandler(handler)
    parser.parse('dblp.xml')
f.close()

with open('authors.txt', 'w', encoding='utf-8') as f:
    for k, v in handler.dict.items():
        f.write(str(v))
        f.write(' ' + k)
        f.write('\n')
    print("done")
f.close()
