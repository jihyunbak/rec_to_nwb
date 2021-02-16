import logging.config
import os

import pandas as pd
from rec_to_binaries.read_binaries import readTrodesExtractedDataFile

from rec_to_nwb.processing.nwb.common.timestamps_manager import TimestampManager

path = os.path.dirname(os.path.abspath(__file__))

logging.config.fileConfig(fname=str(path) + '/../../../../logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


class OldPosTimestampManager(TimestampManager):
    def __init__(self, directories, continuous_time_directories=None):
        # continuous_time_directories is not used in this class
        TimestampManager.__init__(self, directories, continuous_time_directories)

    # override
    def _get_timestamps(self, dataset_id):
        pos_online = readTrodesExtractedDataFile(self.directories[dataset_id][0])
        position = pd.DataFrame(pos_online['data'])
        return position.time.to_numpy(dtype='int64')

    # override for old dataset only
    # --- let's test not overriding ---
<<<<<<< Updated upstream
    # def retrieve_real_timestamps(self, dataset_id):
    #     timestamps_ids = self.read_timestamps_ids(dataset_id)
    #     converted_timestamps = np.ndarray(shape=[len(timestamps_ids), ], dtype="float64")
    #     for i, _ in enumerate(timestamps_ids):
    #         value = float('nan')  # just a dummy value for now
    #         converted_timestamps[i] = value
    #     return converted_timestamps
=======
    # note: continuous_time_directories=None gives rise to an error, 
    # when retrieve_real_timestamps is called
    # and self.continuous_time_directories[dataset_id])
    # -----------------------------------
    def retrieve_real_timestamps(self, dataset_id):
        timestamps_ids = self.read_timestamps_ids(dataset_id)
        converted_timestamps = np.ndarray(shape=[len(timestamps_ids), ], dtype="float64")
        for i, _ in enumerate(timestamps_ids):
            value = float('nan')  # just a dummy value for now
            converted_timestamps[i] = value
        return converted_timestamps
>>>>>>> Stashed changes
