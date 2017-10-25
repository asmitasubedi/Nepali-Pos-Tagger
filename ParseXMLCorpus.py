import os
import xml.etree.ElementTree as ET

path = 'H:\\FYP\\nepali pos\\nnc_updated_ah\\nnc_updated_ah\\gc\\books\\'
filelist = os.listdir(path)

tags=[]

for file in filelist:
    filepath = os.path.join(path, file)
    print(filepath)

    tree = ET.parse(filepath)
    root = tree.getroot()

    for data in root.findall('text'):
            for value in data:
                # print(value.tag)
                if (value.tag == 'group'):
                    # for group in value.findall('group'):
                    for body in value.findall('body'):
                        for div in body.findall('div'):
                            for subdiv in div:
                                # print(subdiv.tag)
                                if (subdiv.tag == "head"):
                                    for sentence in subdiv.findall('s'):
                                        # print(sentence.attrib)
                                        for s in sentence:
                                            # print(s.attrib)
                                            if (s.tag == "foreign"):
                                                for words in s.findall('w'):
                                                   tags.append(words.attrib['ctag'])
                                                   print("%s/%s" % (words.text, words.attrib['ctag']), '', end=''),
                                            # print("\n")
                                            if (s.tag == "w"):
                                                tags.append(s.attrib['ctag'])
                                                print("%s/%s" % (s.text, s.attrib['ctag']), '', end=''),
                                                # countTags(tags,s.attrib['ctag'])
                                        print('\n')

                                if (subdiv.tag == "p"):
                                    for sentence in subdiv.findall('s'):
                                        print(sentence.attrib)
                                        for s in sentence:
                                            if (s.tag == "foreign"):
                                                for words in s.findall('w'):
                                                  tags.append(words.attrib['ctag'])
                                                  print("%s/%s" % (words.text, words.attrib['ctag']), '', end=''),
                                                  # countTags(tags,words.attrib['ctag'])
                                            # print("\n")
                                            if (s.tag == "w"):
                                                tags.append(s.attrib['ctag'])
                                                print("%s/%s" % (s.text, s.attrib['ctag']), '', end=''),
                                                # countTags(tags,s.attrib['ctag'])
                                        print('\n')
                if (value.tag == 'body'):
                    # for body in value.findall('body'):
                    for div in value.findall('div'):
                        for subdiv in div:
                            # print(subdiv.tag)
                            if (subdiv.tag == "head"):
                                for sentence in subdiv.findall('s'):
                                    print(sentence.attrib)
                                    for s in sentence:
                                        # print(s.attrib)
                                        if (s.tag == "foreign"):
                                            for words in s.findall('w'):
                                                tags.append(words.attrib['ctag'])
                                                print("%s/%s" % (words.text, words.attrib['ctag']), '', end=''),
                                                # countTags(tags,words.attrib['ctag'])
                                        # print("\n")
                                        if (s.tag == "w"):
                                            tags.append(s.attrib['ctag'])
                                            print("%s/%s" % (s.text, s.attrib['ctag']), '', end=''),
                                            # countTags(tags,s.attrib['ctag'])
                                    print('\n')

                            if (subdiv.tag == "p"):
                                for sentence in subdiv.findall('s'):
                                    print(sentence.attrib)
                                    for s in sentence:
                                        if (s.tag == "foreign"):
                                            for words in s.findall('w'):
                                                tags.append(words.attrib['ctag'])
                                                print("%s/%s" % (words.text, words.attrib['ctag']), '', end=''),
                                                # countTags(tags,words.attrib['ctag'])
                                        # print("\n")
                                        if (s.tag == "w"):
                                            tags.append(s.attrib['ctag'])
                                            print("%s/%s" % (s.text, s.attrib['ctag']), '', end=''),
                                            # countTags(tags,s.attrib['ctag'])
                                    print('\n')


# print(tags)
# output = set()
# for x in tags:
#     output.add(x)
# print("Number of tags:", len(output))
# print (output)