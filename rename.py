import os
import sys
import glob
import fileinput
import re

def replace_words_in_file(file_path, words):
    with open(file_path, 'r') as file:
        content = file.read()
        for word in words:
            content = re.sub(r'\b{}\b'.format(word), 'rl_{}'.format(word), content)
    
    with open(file_path, 'w') as file:
        file.write(content) 
        
        
def replace_words_in_directory(directory_path, words):
    # Walk through the directory
    for root, dirs, files in os.walk(directory_path): 
        if 'external' in root:
            continue
        
        for file in files:
           if file.endswith('.h') or file.endswith('.c'):
               file_path = os.path.join(root, file)
               replace_words_in_file(file_path, words)
               print(f"Processed file: {file_path}")


if __name__ == "__main__":
    
    rl_tokens = list()
    file = open("rl_tokens.txt", 'r')
    tk = file.read()
    for word in tk.split():
        if word not in rl_tokens:
            rl_tokens.append(word)

    
    directory_path = './src/'
    replace_words_in_directory(directory_path, rl_tokens)