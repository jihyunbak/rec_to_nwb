# plots timestamps from nwb file(e-series)
import matplotlib.pyplot as plt
from pynwb import NWBHDF5IO

from ndx_fllab_novela.apparatus import Apparatus, Edge, Node
from ndx_fllab_novela.header_device import HeaderDevice
from ndx_fllab_novela.ntrode import NTrode

nwb_file = NWBHDF5IO('fldatamigration/fl/test/beans20190718.nwb', 'r')
nwbfile_read = nwb_file.read()

timestamp = nwbfile_read.acquisition['e-series'].timestamps

plt.plot(timestamp)
plt.show()