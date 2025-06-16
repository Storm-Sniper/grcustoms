import numpy as np
from gnuradio import gr


class blk(gr.sync_block): 

    def __init__(self, part = "real"):  
        gr.sync_block.__init__(
            self,
            name='Complex Stream Splitter',
            in_sig=[np.complex64], 
            out_sig=[np.float32] 
        )

        self.part = part 

    def work(self, input_items, output_items): 
        data = input_items[0]
        if self.part == 'real':
            output_items [0] [:] = np.real(data)
        else: output_items [0] [:] = np.imag(data)
        return len(output_items[0])
