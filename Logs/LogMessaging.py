from datetime import datetime


def createLogInitiateMessage(ip, port):
    infoType = '[INFO]'
    entity = 'RECEIVER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = "Connected to SENDER (%s %s)"%(ip, str(port))
    return infoType, entity, date, description

def createLogSendConfirmationMessage(ip, port, ipS, portS):
    infoType = '[INFO]'
    entity = 'SENDER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = "Received connection from RECEIVER (%s %s) at (%s %s)" % (ip, str(port), ipS, str(portS))
    return infoType, entity, date, description

def createLogSendReceiverRSA(ip, port):
    infoType = '[INFO]'
    entity = 'RECEIVER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = "RSA key sent by RECEIVER to (%s %s)" % (ip, str(port))
    return infoType, entity, date, description

def createLogReceiveReceiverRSA(ip, port):
    infoType = '[INFO]'
    entity = 'SENDER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = "RSA key received by SENDER from (%s %s)" % (ip, str(port))
    return infoType, entity, date, description

def createLogSendSenderRSA(ip, port):
    infoType = '[INFO]'
    entity = 'SENDER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = "RSA key sent by SENDER to (%s %s)" % (ip, str(port))
    return infoType, entity, date, description

def createLogReceiveSenderRSA(ip, port):
    infoType = '[INFO]'
    entity = 'RECEIVER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = "RSA key received by RECEIVER from (%s %s)" % (ip, str(port))
    return infoType, entity, date, description


def createLogSendIV(ip, port):
    infoType = '[INFO]'
    entity = 'RECEIVER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = "IV sent by RECEIVER to (%s %s)" % (ip, str(port))
    return infoType, entity, date, description

def createLogReceiveIV(ip, port):
    infoType = '[INFO]'
    entity = 'SENDER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = "IV received by SENDER from (%s %s)" % (ip, str(port))
    return infoType, entity, date, description

def createLogSendKey(ip, port):
    infoType = '[INFO]'
    entity = 'SENDER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = "AES KEY sent by SENDER to (%s %s)" % (ip, str(port))
    return infoType, entity, date, description

def createLogReceiveKey(ip, port):
    infoType = '[INFO]'
    entity = 'RECEIVER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = "AES KEY received by RECEIVER from (%s %s)" % (ip, str(port))
    return infoType, entity, date, description

def createLogSendNegociate(ip, port):
    infoType = '[INFO]'
    entity = 'RECEIVER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = "Parameters sent to SENDER (%s %s)" % (ip, str(port))
    return infoType, entity, date, description

def createLogSendBackNegociate(ip, port):
    infoType = '[INFO]'
    entity = 'SENDER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = "Parameters corrected sent back to RECEIVER (%s %s)" % (ip, str(port))
    return infoType, entity, date, description


def createLogSendOT(ip, port):
    infoType = '[INFO]'
    entity = 'RECEIVER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = "OT Content sent to SENDER (%s %s)" % (ip, str(port))
    return infoType, entity, date, description

def createLogSendPRFKey(ip, port):
    infoType = '[INFO]'
    entity = 'RECEIVER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = "PRF Key sent to SENDER (%s %s)" % (ip, str(port))
    return infoType, entity, date, description

def createLogSendPsiValues(ip, port):
    infoType = '[INFO]'
    entity = 'SENDER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = "Psi Values sent to RECEIVER (%s %s)" % (ip, str(port))
    return infoType, entity, date, description

def createLogReceiveInitConnection(ip, port):
    infoType = '[INFO]'
    entity = 'SENDER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = "Received connection from RECEIVER (%s, %s)" % (ip, str(port))
    return infoType, entity, date, description

def createLogReceiveNegParameters(ip, port):
    infoType = '[INFO]'
    entity = 'SENDER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = "Received parameters from RECEIVER (%s, %s)" % (ip, str(port))
    return infoType, entity, date, description

def createModifiedLogReceiveNegParameters(ip, port):
    infoType = '[INFO]'
    entity = 'RECEIVER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = "Received modified parameters from SENDER (%s, %s)" % (ip, str(port))
    return infoType, entity, date, description

def createLogReceiveOT(ip, port):
    infoType = '[INFO]'
    entity = 'SENDER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = "Received OT data from RECEIVER (%s, %s)" % (ip, str(port))
    return infoType, entity, date, description

def createLogReceivePRFKey(ip, port):
    infoType = '[INFO]'
    entity = 'SENDER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = "Received PRF key data from RECEIVER (%s, %s)" % (ip, str(port))
    return infoType, entity, date, description

def createLogReceivePsi(ip, port):
    infoType = '[INFO]'
    entity = 'RECEIVER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = "Received PSI data from SENDER (%s, %s)" % (ip, str(port))
    return infoType, entity, date, description

def createLogReceiveConfirmConnection(ip, port):
    infoType = '[INFO]'
    entity = 'RECEIVER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = "Received confirmation from SENDER (%s, %s)" % (ip, str(port))
    return infoType, entity, date, description




# -----------------------------------------

def firstHashWrong(lambdax):
    infoType = '[WARNING]'
    entity = 'SENDER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = 'First hash function is not corresponding with lambda '+str(lambdax)+' chosen'
    return "%s %s %s %s"%(infoType, entity, date, description), infoType, entity, date, description

def secondHashWrong():
    infoType = '[WARNING]'
    entity = 'SENDER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = 'Second hash function is not valid'
    return "%s %s %s %s"%(infoType, entity, date, description), infoType, entity, date, description

def prfWrong(lambdax):
    infoType = '[WARNING]'
    entity = 'SENDER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = 'PRF is not valid for '+str(lambdax)+ 'selected'
    return "%s %s %s %s"%(infoType, entity, date, description), infoType, entity, date, description

def otVariantWrong():
    infoType = '[WARNING]'
    entity = 'SENDER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = 'OT Variants not valid; please select 1 or 2'
    return "%s %s %s %s"%(infoType, entity, date, description),infoType, entity, date, description

def lambdaWrong(listx):
    infoType = '[WARNING]'
    entity = 'SENDER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = 'Lambda is not an accepted value! Please insert a value from '+str(listx)
    return "%s %s %s %s"%(infoType, entity, date, description), infoType, entity, date, description

def sigmaLow():
    infoType = '[WARNING]'
    entity = 'SENDER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = 'Sigma too low; please select a value higher than 40'
    return "%s %s %s %s"%(infoType, entity, date, description),infoType, entity, date, description

def sigmaWrong():
    infoType = '[WARNING]'
    entity = 'SENDER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = 'Invalid sigma'
    return "%s %s %s %s"%(infoType, entity, date, description),infoType, entity, date, description

def wLow():
    infoType = '[WARNING]'
    entity = 'SENDER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = 'W too low; please select a value higher at least than 10'
    return "%s %s %s %s"%(infoType, entity, date, description), infoType, entity, date, description

def wWrong():
    infoType = '[WARNING]'
    entity = 'SENDER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = 'Invalid W'
    return "%s %s %s %s"%(infoType, entity, date, description), infoType, entity, date, description

def mLow():
    infoType = '[WARNING]'
    entity = 'SENDER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = 'M not between 0.25 and 1.25'
    return "%s %s %s %s"%(infoType, entity, date, description),infoType, entity, date, description

def mWrong():
    infoType = '[WARNING]'
    entity = 'SENDER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = 'Invalid M'
    return "%s %s %s %s"%(infoType, entity, date, description), infoType, entity, date, description



def exceptionReceiver(e):
    infoType = '[ERROR]'
    entity = 'RECEIVER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = str(e)
    return infoType, entity, date, description

def receivedExceptionFromReceiver(e):
    infoType = '[ERROR FROM RECEIVER]'
    entity = 'SENDER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = str(e)
    return infoType, entity, date, description

def exceptionSender(e):
    infoType = '[ERROR]'
    entity = 'SENDER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = str(e)
    return infoType, entity, date, description

def receivedExceptionFromSender(e):
    infoType = '[ERROR FROM SENDER]'
    entity = 'RECEIVER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = str(e)
    return infoType, entity, date, description