import Sender
import Receiver
import Entity
import Transfer


t1 = Transfer.Transfer_Protocol("t1 param")
t2 = Transfer.Transfer_Protocol("t2 param")

# Entity.Entity.__init__.calls.clear()
# print(Entity.Entity.__init__.calls)

receiver = Receiver.Receiver(t2)
sender = Sender.Sender(t1)

print()
print("R: ", receiver.transfer_protocol.parameters)
print("S: ", sender.transfer_protocol.parameters)
