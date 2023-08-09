import os
import keyInfo

def order(command):
    os.system(command)

def createDataset():
    command = 'openai tools fine_tunes.prepare_data -f '
    command += keyInfo.dataset
    os.system(command)

def createFinetune():
    command = 'openai --api-key '
    command += keyInfo.apiKey
    command += ' api fine_tunes.create -t '
    command += keyInfo.dataset
    command += ' -m '
    command += keyInfo.model
    os.system(command)

def continueFinetune():
    command = 'openai --api-key '
    command += keyInfo.apiKey
    command += ' api fine_tunes.follow -i '
    command += keyInfo.jobId
    return os.popen(command).read()

def loopFinetune():
    res = continueFinetune()
    print(res)
    cnt = 1
    while True:
        cnt += 1
        if 'Stream interrupted' in res:    
            print('finetune api loop ', cnt, ' times ..')
            res = continueFinetune()
            print(res)
        else:
            print(res)
            break
 
createFinetune()