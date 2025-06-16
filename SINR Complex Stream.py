import numpy as np
from gnuradio import gr


class blk(gr.sync_block):

    def __init__(self):  
        gr.sync_block.__init__(
            self,
            name='SINR Complex Input Streams',  
            in_sig=[np.complex64, np.complex64],
            out_sig=[np.float32] 
        )

    def work(self, input_items, output_items):
        signalNoise = input_items[0]
        noise = input_items[1]
        finalSINR = output_items[0]

        minLength = min(len(signalNoise), len(noise))

        powerSignalNoise = np.abs(signalNoise [:N])**2
        powerNoise = np.abs(noise [:N])**2 + (1e-12)

        linearSINR = powerSignalNoise / powerNoise

        decibelSINR = 10*(np.log10(linearSINR))

        finalSINR [:N] = decibelSINR

