###!/usr/local/opt/python/bin/python3.7
#import sys
#print("If the interpreter doesn't work, replace the line below with: #!" + str(sys.executable))

from text_normalization.normalization_tools import Text
import argparse

'''n_args = len(sys.argv) -1

if (n_args<1 or n_args>4):
    print ("ERROR: \t Usage ./normalize.py <path_to_text_to_normalize>  <language> <sentence_delimiters> <path_to_output_file>")
    print("where language can be either <pt>(for portuguese) or <en>(for english) or <fr>(for french) or <es>(for spanish)")
    print("and sentence_delimiters can be any punctuation that your texts uses to divide sentences")
    print("language and sentence delimiters are OPTIONAL arguments")
    sys.exit(1)

txt = sys.argv[1]

if n_args==1:
    my_text = Text(txt)
elif n_args==2:
    lang = sys.argv[2]
    my_text = Text(txt,lang)
elif n_args==3 :
    lang = sys.argv[2]
    dlmtrs = sys.argv[3]
    my_text = Text(txt, lang, dlmtrs)
'''
parser = argparse.ArgumentParser(description='Description')

parser.add_argument('--text',type=str)
parser.add_argument('--language',type=str)
parser.add_argument('--delimiters',type=str)

args = parser.parse_args()
if args.text is None:
    print('ERROR: Usage python3 normalize.py --text <path_to_text> --language <en OR fr OR pt OR es> --delimiters <a set of punctuation> ')
    print('Example: python3 normalize.py --text ~/Desktop/text --language pt --delimiters .!?')
    print('Arguments language and delimiters are optional')
    exit(1)

if (args.language is None) and (args.delimiters is None):
    my_text = Text(args.text)
elif (args.language is None) and (args.delimiters is not None):
    my_text = Text(args.text, sentence_delimiters= args.delimiters)
elif (args.language is not None) and (args.delimiters is None):
    my_text = Text(args.text, lang= args.lanuage)
else:
    my_text = Text(args.text, lang=args.language, sentence_delimiters= args.delimiters)



