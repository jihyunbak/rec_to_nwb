import os
import unittest

from rec_to_binaries import extract_trodes_rec_file

path = os.path.dirname(os.path.abspath(__file__))

_DEFAULT_TRODES_REC_EXPORT_ARGS = ('-reconfig', str(path) + '/../processing/res/reconfig_header.xml')


class TestRecToBinGeneration(unittest.TestCase):

    @unittest.skip("Super heavy REC to Preprocessing Generation")
    def test_generation_preprocessing(self):
        extract_trodes_rec_file(
            data_dir='../test_data/',
            animal='beans',
            parallel_instances=4,
            analog_export_args=_DEFAULT_TRODES_REC_EXPORT_ARGS,
            overwrite=True,
            extract_spikes=False,
            extract_analog=True,
            extract_mda=True,
            extract_lfps=False,
            extract_dio=True,
        )

        self.assertTrue(os.path.isdir('/../test_data/beans/preprocessing'))
        self.assertTrue(os.path.isdir('/../test_data/beans/preprocessing/' + "20190718"))
