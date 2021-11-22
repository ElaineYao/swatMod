
"""
swat-s1 plc2
"""

from minicps.devices import PLC
from utils import PLC2_DATA, STATE, PLC2_PROTOCOL
from utils import PLC_SAMPLES, PLC_PERIOD_SEC
from utils import IP

import time

PLC1_ADDR = IP['plc1']
PLC2_ADDR = IP['plc2']
PLC3_ADDR = IP['plc3']

# Elaine --version
send_FIT201_2 = ('HR', 0, 'FIT201')
# send_FIT201_2 = ('CO', 0, 'FIT201')
get_FIT201_2 = ('FIT201', 2)
# FIT201_2 = ('FIT201', 2)


class SwatPLC2(PLC):

    def pre_loop(self, sleep=0.1):
        print ('DEBUG: swat-s1 plc2 enters pre_loop')
        print()

        time.sleep(sleep)

    def main_loop(self):
        """plc2 main loop.

            - read flow level sensors #2
            - update interal enip server
        """

        print ('DEBUG: swat-s1 plc2 enters main_loop.')
        print()

        count = 0
        while(count <= PLC_SAMPLES):

            fit201 = int(float(self.get(get_FIT201_2)))
            print(("DEBUG PLC2 - get fit201: %f" % fit201))
            # fit201 = True
            self.send(send_FIT201_2, fit201, (PLC2_ADDR+ ':502'))
            # self.send(send_FIT201_2, fit201, ('localhost:502'))
            print(("DEBUG PLC2 - send fit201: ", fit201))
            fit201 = self.receive(send_FIT201_2, (PLC2_ADDR+ ':502'))
            print(("DEBUG PLC2 - receive fit201: ", fit201))

            time.sleep(PLC_PERIOD_SEC)
            count += 1

        print ('DEBUG swat plc2 shutdown')


if __name__ == "__main__":

    # notice that memory init is different form disk init
    plc2 = SwatPLC2(
        name='plc2',
        state=STATE,
        protocol=PLC2_PROTOCOL,
        memory=PLC2_DATA,
        disk=PLC2_DATA)
