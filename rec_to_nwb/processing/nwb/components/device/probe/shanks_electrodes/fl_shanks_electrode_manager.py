from rec_to_nwb.processing.nwb.components.device.probe.shanks_electrodes.fl_shanks_electrode_builder import \
    FlShanksElectrodeBuilder
from rec_to_nwb.processing.tools.beartype.beartype import beartype
from rec_to_nwb.processing.tools.filter_probe_by_type import filter_probe_by_type


class FlShanksElectrodeManager:

    @beartype
    def __init__(self, probes_metadata: list, electrode_groups_metadata: list):
        self.probes_metadata = probes_metadata
        self.electrode_groups_metadata = electrode_groups_metadata

        self.fl_shanks_electrodes_builder = FlShanksElectrodeBuilder()

    @beartype
    def get_fl_shanks_electrodes_dict(self) -> dict:
        fl_shanks_electrodes_dict = {}
        probes_types = []
        for electrode_group_metadata in self.electrode_groups_metadata:
            if electrode_group_metadata['device_type'] not in probes_types:
                fl_shanks_electrodes = []
                probes_types.append(electrode_group_metadata['device_type'])
                probe_metadata = filter_probe_by_type(self.probes_metadata, electrode_group_metadata['device_type'])

                fl_shanks_electrodes.extend(self.__build_fl_shanks_electrodes(probe_metadata))
                fl_shanks_electrodes_dict[electrode_group_metadata['device_type']] = fl_shanks_electrodes
        return fl_shanks_electrodes_dict

    def __build_fl_shanks_electrodes(self, probe_metadata):

        for shank in probe_metadata['shanks']:
            for electrode in shank['electrodes']:
                yield self.__build_single_fl_shanks_electrodes(electrode)

    def __build_single_fl_shanks_electrodes(self, electrode):
        return self.fl_shanks_electrodes_builder.build(electrode)