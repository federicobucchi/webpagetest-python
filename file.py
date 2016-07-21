import json

def createFile(filename, content):
    with open('./' + filename + '.json', 'w') as outfile:
        json.dump(content, outfile)
    outfile.close()
