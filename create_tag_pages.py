#!/usr/bin/env python

import glob
import os

TAG_PAGE_TEMPLATE = '---\nlayout: tagpage\ntitle: "{}"\n---\n'

def collect_tags(filename, tag_array):
    """Collect the tags listed in this post and add them to 'tag_array'"""
    print(filename)
    with open(filename, 'r') as f:
        crawl = False
        for line in f:
            if line.strip() == '---':
                if not crawl:
                    crawl = True
                else:
                    crawl = False
                    break
            elif crawl:
                current_tags = line.strip().split()
                if current_tags[0] == 'tags:':
                    for line in f:
                        tag_line = line.strip().split()
                        if tag_line[0] == '-':
                            tag_array.append(tag_line[1].strip('"'))
                        else:
                            crawl = False
                            break
                    break
        print('Collected tags:')
        print(tag_array)

post_dir = '_posts/'
tag_dir = 'tags/'

post_files = glob.glob(post_dir + '*md')

tags = []
for file in post_files:
    collect_tags(file, tags)

if not os.path.exists(tag_dir):
    os.makedirs(tag_dir)

print("\n{} tag pages have been generated:".format(len(tags)))

for tag in tags:
    tag_filename = tag if tag[0] != '#' else tag[1:]
    tag_filename = tag_dir + tag_filename + '.md'
    print("  {}".format(tag_filename))
    with open(tag_filename, 'w') as f:
        f.write(TAG_PAGE_TEMPLATE.format(tag))

print('')
