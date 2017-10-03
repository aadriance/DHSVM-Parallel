import filecmp
import resource
import subprocess

def runDHSVM():
    cmd = ['./DHSVM3.1.2', '../INPUT.Mercer.3.1.2_Bin']
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, cwd='sourcecode')
    process.wait()
    #for line in process.stdout:
    #    print(line)
    info = resource.getrusage(resource.RUSAGE_CHILDREN)
    print('\nRan for ', info.ru_utime, ' seconds.')

def compareFiles():
    filesToCompare = ['Aggregated.Values',
        'ATP.Only',
        'Beam.Only',
        'Diffuse.Only',
        'ILW.Only',
        'Inflow.Only',
        'ISW.Only',
        'Mass.Balance',
        'Mass.Final.Balance',
        'NLW.Only',
        'NSW.Only',
        'Outflow.Only',
        'Skyview.Only',
        'Stream.Flow',
        'Streamflow.Only',
        'VP.Only',
        'WND.Only']
    truthFolder = 'ValidOut'
    compareFolder = 'output'
    match, mismatch, errors = filecmp.cmpfiles(truthFolder, compareFolder, filesToCompare, shallow=True)
    print('Mismatched: ', mismatch)
    print('Errored: ', errors)

if __name__ == '__main__':
    runDHSVM()
    compareFiles()