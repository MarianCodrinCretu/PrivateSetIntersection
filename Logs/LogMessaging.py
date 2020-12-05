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

def exceptionReceiver(e):
    infoType = '[ERROR]'
    entity = 'RECEIVER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = str(e)
    return infoType, entity, date, description

def exceptionSender(e):
    infoType = '[ERROR]'
    entity = 'SENDER'
    date = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
    description = str(e)
    return infoType, entity, date, description