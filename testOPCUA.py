from opcua import Client
import schedule
import time

client = Client('opc.tcp://10.1.10.200:4840')
client.connect()

i1 = 0


def grabData():
    global i1
    obj0 = client.get_node('ns=2;s=SR_Main.faux_Output1')
    obj1 = client.get_node('ns=2;s=SR_Main.faux_Output2')
    obj2 = client.get_node('ns=2;s=SR_Main.testStr')
    # print("Objects node value is: ", obj0.get_value())
    print("Current Temperature is: ", obj1.get_value())
    print('Count: ', i1)
    i1 = i1 + 1
    # print("Objects node value is: ", obj2.get_value())


schedule.every(2).seconds.do(grabData)

try:
    while 1:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    client.disconnect()
    client.close_session()
    print('----------')
    print('Keyboard Interrupted!')
    print('----------')

# client.disconnect()
# client.close_session()
