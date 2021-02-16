import logging.config
import os

from rec_to_binaries.read_binaries import readTrodesExtractedDataFile

from rec_to_nwb.processing.time.continuous_time_extractor import ContinuousTimeExtractor
from rec_to_nwb.processing.time.timestamp_converter import TimestampConverter

path = os.path.dirname(os.path.abspath(__file__))
logging.config.fileConfig(fname=str(path) + '/../../../../logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


class FlAnalogExtractor:

    @staticmethod
    def extract_analog_for_single_dataset(analog_files, continuous_time_file=None):
        single_dataset_data = {}
        for analog_file in analog_files:
            if not 'timestamps' in analog_file:
                analog_data = readTrodesExtractedDataFile(analog_files[analog_file])
                values = analog_data['data']
                single_dataset_data[analog_data['id']] = values
            else:
                if continuous_time_file:
                    single_dataset_data[analog_file] = FlAnalogExtractor._extract_analog_file(
                                        analog_files[analog_file], continuous_time_file)
                else:
                    single_dataset_data[analog_file] = FlAnalogExtractor._extract_analog_file_old(
                                        analog_files[analog_file])
        return single_dataset_data

    @staticmethod
    def _extract_analog_file(analog_file_value, continuous_time_file):
        continuous_time = ContinuousTimeExtractor.get_continuous_time_array_file(continuous_time_file)
        timestamps = readTrodesExtractedDataFile(analog_file_value)['data']['time']
        return TimestampConverter.convert_timestamps(continuous_time, timestamps)
        
    @staticmethod
    def _extract_analog_file_old(analog_file_value):
        analog_data = readTrodesExtractedDataFile(analog_file_value)
        timestamps = analog_data['data']
        # not converted
        return timestamps
