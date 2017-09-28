import filecmp

def compareFiles():
    filesToCompare = ['Aggregated.Values']
    truthFolder = 'ValidOut'
    compareFolder = 'output'
    match, mismatch, errors = filecmp.cmpfiles(truthFolder, compareFolder, filesToCompare, shallow=True)
    print('Mismatched: ', mismatch)

if __name__ == '__main__':
    compareFiles()