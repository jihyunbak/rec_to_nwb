from rec_to_nwb.processing.nwb.components.mda.fl_mda_builder import FlMdaBuilder
from rec_to_nwb.processing.nwb.components.mda.old_fl_mda_extractor import OldFlMdaExtractor
from rec_to_nwb.processing.nwb.components.mda.table_region_builder import TableRegionBuilder


class OldFlMdaManager:
    def __init__(self, nwb_content, sampling_rate, datasets, conversion):
        self.__table_region_builder = TableRegionBuilder(nwb_content)
        self.__fl_mda_extractor = OldFlMdaExtractor(datasets, conversion)
        # we converted the data to uV in the extractor, so the conversion to V is always 1e-6
        self.__fl_mda_builder = FlMdaBuilder(sampling_rate, 0.000001)

    def get_data(self):
        electrode_table_region = self.__table_region_builder.build()
        data = self.__fl_mda_extractor.get_data()
        return self.__fl_mda_builder.build(electrode_table_region, data)
