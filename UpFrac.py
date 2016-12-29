#copy modelData modules from UDEC to HOMOGENIZE
import os
import sys
import shutil
import time
import psutil
import importlib
import argparse

def main():
    
    pass 
    
def importModelData(modelName):
    global modelData
    modelData = importlib.import_module('Data.Model.'+modelName)
    
def run(modelName, radius=10):
    importModelData(modelName)
    main(radius)
    
#TODO: move handlers to module files
 
def udecHandler(args):
    if res.unity_deploy:
        print('Unity deploy')

    if res.unity_tagcheck:
        print('Unity tagcheck')
        
def hodsHandler(args):      
    def main(revCentreX=None, revCentreY=None, revRadius=None):
    os.system('cls')

    if revCentreX == None:
        revCentreX = modelData.modelSize/2
    if revCentreY == None:
        revCentreY = modelData.modelSize/2
    if revRadius == None:
        revRadius = modelData.modelSize/2-modelData.blockSize*2
    revCentre = {'x':revCentreX, 'y':revCentreY}

    from Modules import Module_HODS  
    for j in range(len(modelData.confiningStress)):
        fileName = '{0}({1}.{2})'.format(args.name, 0, j)
        M = ModuleHODS.Module_HODS(fileName)
        # stressHistory = H.stress()
        # strainHistory = H.strain()
        # timeHistory = H.time()
        
        # writeToFile(timeHistory, stressHistory, strainHistory, j, i, interpolate=interpolate)
        # print (' ')
            
    # main()           
def ostrichHandler(args):
    if res.clc_deploy:
        print('Clc deploy')
        
        
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='MOUSE: An Up-Scaling Utility for DEM Simulations')
    #parser.add_argument('-n', '--name', required=True ,help='Name of the file containing the model data without the extension')

    subparsers = parser.add_subparsers()
    
    #TODO: import subparsers form module files
    
    udecParser = subparsers.add_parser('UDEC')
    udecParser.set_defaults(func=udecHandler)
    
    hodsParser = subparsers.add_parser('HODS')
    
    from Modules import Module_HODS    
    hodsParser = Module_HODS.populateArgumentParser(hodsParser)
    #hodsParser.set_defaults(func=hodsHandler)
    
    ostrichParser = subparsers.add_parser('OSTRICH')
    ostrichParser.add_argument('-id', '--identity', help='identification Number')
    ostrichParser.add_argument('-o', '--optimizer', default='ParticleSwarm', help='optimization algorithm')
    
    args = parser.parse_args()
    args.func(args)


    

    
    

def main(radius, optimizer='ParticleSwarm'): #identity=None, 
    """
    docstgring
    """
    os.system('cls')
    if radius:
        os.system('python ostrichHomogenize.py -n {0} -r {1}'.format(modelData.modelName, radius))
    else:
        os.system('python ostrichHomogenize.py -n {0}'.format(modelData.modelName))
    parameterizationRun = 1
    for i in range(len(modelData.simulationTime)):
        simulationName = '{0}({1}.'.format(modelData.modelName, i, 0)
        print('*'*70)
        print('OSTRICH file setup for {0} set {1}'.format(modelData.modelName, parameterizationRun))
        print('*'*70)
        print('Filling in model templates...')
        os.system('python createOstrichInput.py -n {0} -r {1} -o {2}'.format(modelData.modelName, parameterizationRun, optimizer))
        print('\tDone')
        os.chdir(os.path.join(os.getcwd(), 'OSTRICH'))
        print('Cleaning up OSTRICH mess from previous run...')
        os.system('cleanup.bat')
        for j in range(len(modelData.confiningStress)):
            open(os.path.join('fittedHistory', '{0}({1}.{2})_{3}_fittedHistory.pkl'.format(modelData.modelName, i, j, modelData.abaqusMaterial)), 'w').close()
        print('\tDone')
        print('Initializing OSTRICH...' )
        print('\tDone')
        MPI = True #add as a CLA
        if MPI:
            print('Running OSTRICH MPI...\n\t', end='')
            os.system('mpirun.bat >NUL 2>OstErrors.log')
            while 1: 
                try:
                    with open('OstStatus0.txt', 'r') as file:
                        lines = file.readlines()
                        comp = int(float(lines[2][18:-1]))
                        numString = '{0}%'.format(comp)
                        print(numString, end='')
                        print('\b'*len(numString), end='')
                        sys.stdout.flush()
                        if comp == 100:
                            print('100%')
                            print('Computing parameter statistics...')
                            while 1:
                                runningProcesses = psutil.pids()
                                br = True
                                for k in runningProcesses:
                                    try:
                                        if psutil.Process(k).name() == 'OstrichMPI.exe':
                                            br = False
                                    except:
                                        pass
                                if br:
                                    break
                            print('\tDone')        
                            print('Shutting Down OSTRICH...\n\t', end='')
                            sleepTime = 10
                            for k in range(sleepTime):
                                time.sleep(1)
                                numString = '{0}%'.format(int(k/sleepTime*100))
                                print(numString, end='')
                                print('\b'*len(numString), end='')
                                sys.stdout.flush()
                            print('100%')
                            break
                except (FileNotFoundError, IndexError, PermissionError):
                    pass
                time.sleep(1)
        else:
            print('Running Serial OSTRICH')
            os.system('ostrich.exe')
            print('\tDone')
            print('Shutting Down OSTRICH...')
            print('\Done')
        os.chdir(os.pardir)
        
        print('Saving estimated parameter set')
        if radius:
            shutil.copy(os.path.join('OSTRICH', 'OstOutput0.txt'), os.path.join('OSTRICH', 'ostOutput', 'OstOutput_{0}_{1}_{2}_radius-{3}.txt'.format(modelData.modelName, modelData.abaqusMaterial, parameterizationRun, radius)))
        if identity:
            shutil.copy(os.path.join('OSTRICH', 'OstOutput0.txt'), os.path.join('OSTRICH', 'ostOutput', 'OstOutput_{0}_{1}_{2}_{3}_id-{4}.txt'.format(modelData.modelName, modelData.abaqusMaterial, parameterizationRun, optimizer, identity)))            
        else:
            shutil.copy(os.path.join('OSTRICH', 'OstOutput0.txt'), os.path.join('OSTRICH', 'ostOutput', 'OstOutput_{0}_{1}_{2}.txt'.format(modelData.modelName, modelData.abaqusMaterial, parameterizationRun)))
        print('\tDone\n')
      
        parameterizationRun +=1
    os.chdir(os.path.join(os.getcwd(), 'OSTRICH'))
    os.system('cleanup.bat')
    os.chdir(os.pardir)
