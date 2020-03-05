import os
from datetime import datetime
from unittest import TestCase
from unittest.mock import Mock

from dateutil.tz import tzlocal
from hdmf.common import DynamicTable, VectorData, ElementIdentifiers
from pynwb import NWBFile

from ndx_fllab_novela.fl_electrode_group import FLElectrodeGroup
from testfixtures import should_raise

from fl.datamigration.exceptions.none_param_in_init_exception import NoneParamInInitException
from fl.datamigration.nwb.components.electrodes.fl_electrode_manager import FlElectrodeManager

path = os.path.dirname(os.path.abspath(__file__))


class TestFlElectrodeManager(TestCase):

    def test_manager_builds_FlElectrodes_successfully(self):
        electrode_groups_metadata = [
            {'id': 0, 'location': 'mPFC', 'device_type': 'tetrode_12.5', 'description': 'Probe 1'},
            {'id': 1, 'location': 'mPFC', 'device_type': '128c-4s8mm6cm-20um-40um-sl', 'description': 'Probe 2'}]

        probes_metadata = [{'probe_type': 'tetrode_12.5', 'contact_size': 20.0, 'num_shanks': 1,
                            'shanks': [
                                {'shank_id': 0,
                                 'electrodes': [
                                     {'id': 0, 'rel_x': 0, 'rel_y': 0, 'rel_z': 0},
                                     {'id': 1, 'rel_x': 0, 'rel_y': 0, 'rel_z': 0},
                                     {'id': 2, 'rel_x': 0, 'rel_y': 0, 'rel_z': 0},
                                     {'id': 3, 'rel_x': 0, 'rel_y': 0, 'rel_z': 0}]}]},
                           {'probe_type': '128c-4s8mm6cm-20um-40um-sl', 'contact_size': 20.0, 'num_shanks': 4,
                            'shanks': [
                                {'shank_id': 0, 'electrodes': [
                                    {'id': 0, 'rel_x': 0, 'rel_y': 0, 'rel_z': 0},
                                    {'id': 1, 'rel_x': 40, 'rel_y': 0, 'rel_z': 0}]},
                                {'shank_id': 1, 'electrodes': [
                                    {'id': 32, 'rel_x': 0, 'rel_y': 300, 'rel_z': 0},
                                    {'id': 33, 'rel_x': 40, 'rel_y': 300, 'rel_z': 0}]},
                                {'shank_id': 2, 'electrodes': [
                                    {'id': 64, 'rel_x': 0, 'rel_y': 600, 'rel_z': 0},
                                    {'id': 65, 'rel_x': 40, 'rel_y': 600, 'rel_z': 0}, ]},
                                {'shank_id': 3, 'electrodes': [
                                    {'id': 96, 'rel_x': 0, 'rel_y': 900, 'rel_z': 0},
                                    {'id': 97, 'rel_x': 40, 'rel_y': 900, 'rel_z': 0}]}]}
                           ]

        mock_eg_1 = Mock()
        mock_eg_2 = Mock()
        mock_eg_1.__class__ = FLElectrodeGroup
        mock_eg_2.__class__ = FLElectrodeGroup
        mock_eg_1.name = 'FLElectrodeGroup1'
        mock_eg_2.name = 'FLElectrodeGroup2'

        fl_electrodes_manager = FlElectrodeManager(probes_metadata, electrode_groups_metadata)

        fl_electrodes = fl_electrodes_manager.get_fl_electrodes(
            electrode_groups=[mock_eg_1, mock_eg_2],
        )

        self.assertEqual(12, len(fl_electrodes))

        self.assertIsInstance(fl_electrodes, list)
        self.assertIsInstance(fl_electrodes[0].electrode_group, FLElectrodeGroup)

        self.assertEqual(fl_electrodes[0].electrode_group, mock_eg_1)
        self.assertEqual(fl_electrodes[1].electrode_group, mock_eg_1)
        self.assertEqual(fl_electrodes[2].electrode_group, mock_eg_1)
        self.assertEqual(fl_electrodes[3].electrode_group, mock_eg_1)

        self.assertEqual(fl_electrodes[4].electrode_group, mock_eg_2)
        self.assertEqual(fl_electrodes[5].electrode_group, mock_eg_2)
        self.assertEqual(fl_electrodes[6].electrode_group, mock_eg_2)

    @should_raise(NoneParamInInitException)
    def test_manager_fails_creating_FlElectrodes_due_to_None_param(self):
        probes_metadata = [{'probe_type': 'tetrode_12.5', 'contact_size': 20.0, 'num_shanks': 1,
                            'shanks': [
                                {'shank_id': 0,
                                 'electrodes': [
                                     {'id': 0, 'rel_x': 0, 'rel_y': 0, 'rel_z': 0},
                                     {'id': 1, 'rel_x': 0, 'rel_y': 0, 'rel_z': 0},
                                     {'id': 2, 'rel_x': 0, 'rel_y': 0, 'rel_z': 0},
                                     {'id': 3, 'rel_x': 0, 'rel_y': 0, 'rel_z': 0}]}]},
                           {'probe_type': '128c-4s8mm6cm-20um-40um-sl', 'contact_size': 20.0, 'num_shanks': 4,
                            'shanks': [
                                {'shank_id': 0, 'electrodes': [
                                    {'id': 0, 'rel_x': 0, 'rel_y': 0, 'rel_z': 0},
                                    {'id': 1, 'rel_x': 40, 'rel_y': 0, 'rel_z': 0}]},
                                {'shank_id': 1, 'electrodes': [
                                    {'id': 32, 'rel_x': 0, 'rel_y': 300, 'rel_z': 0},
                                    {'id': 33, 'rel_x': 40, 'rel_y': 300, 'rel_z': 0}]},
                                {'shank_id': 2, 'electrodes': [
                                    {'id': 64, 'rel_x': 0, 'rel_y': 600, 'rel_z': 0},
                                    {'id': 65, 'rel_x': 40, 'rel_y': 600, 'rel_z': 0}, ]},
                                {'shank_id': 3, 'electrodes': [
                                    {'id': 96, 'rel_x': 0, 'rel_y': 900, 'rel_z': 0},
                                    {'id': 97, 'rel_x': 40, 'rel_y': 900, 'rel_z': 0}]}]}
                           ]

        mock_eg_1 = Mock()
        mock_eg_2 = Mock()
        mock_eg_1.__class__ = FLElectrodeGroup
        mock_eg_2.__class__ = FLElectrodeGroup
        mock_eg_1.name = 'FLElectrodeGroup1'
        mock_eg_2.name = 'FLElectrodeGroup2'

        fl_electrodes_manager = FlElectrodeManager(probes_metadata, None)

        fl_electrodes_manager.get_fl_electrodes(
            electrode_groups=[mock_eg_1, mock_eg_2],
        )

    @should_raise(NoneParamInInitException)
    def test_manager_fails_creating_FlElectrodes_due_to_None_ElectrodeGroup(self):
        electrode_groups_metadata = [
            {'id': 0, 'location': 'mPFC', 'device_type': 'tetrode_12.5', 'description': 'Probe 1'},
            {'id': 1, 'location': 'mPFC', 'device_type': '128c-4s8mm6cm-20um-40um-sl', 'description': 'Probe 2'}]

        probes_metadata = [{'probe_type': 'tetrode_12.5', 'contact_size': 20.0, 'num_shanks': 1,
                            'shanks': [
                                {'shank_id': 0,
                                 'electrodes': [
                                     {'id': 0, 'rel_x': 0, 'rel_y': 0, 'rel_z': 0},
                                     {'id': 1, 'rel_x': 0, 'rel_y': 0, 'rel_z': 0},
                                     {'id': 2, 'rel_x': 0, 'rel_y': 0, 'rel_z': 0},
                                     {'id': 3, 'rel_x': 0, 'rel_y': 0, 'rel_z': 0}]}]},
                           {'probe_type': '128c-4s8mm6cm-20um-40um-sl', 'contact_size': 20.0, 'num_shanks': 4,
                            'shanks': [
                                {'shank_id': 0, 'electrodes': [
                                    {'id': 0, 'rel_x': 0, 'rel_y': 0, 'rel_z': 0},
                                    {'id': 1, 'rel_x': 40, 'rel_y': 0, 'rel_z': 0}]},
                                {'shank_id': 1, 'electrodes': [
                                    {'id': 32, 'rel_x': 0, 'rel_y': 300, 'rel_z': 0},
                                    {'id': 33, 'rel_x': 40, 'rel_y': 300, 'rel_z': 0}]},
                                {'shank_id': 2, 'electrodes': [
                                    {'id': 64, 'rel_x': 0, 'rel_y': 600, 'rel_z': 0},
                                    {'id': 65, 'rel_x': 40, 'rel_y': 600, 'rel_z': 0}, ]},
                                {'shank_id': 3, 'electrodes': [
                                    {'id': 96, 'rel_x': 0, 'rel_y': 900, 'rel_z': 0},
                                    {'id': 97, 'rel_x': 40, 'rel_y': 900, 'rel_z': 0}]}]}
                           ]

        fl_electrodes_manager = FlElectrodeManager(probes_metadata, electrode_groups_metadata)

        fl_electrodes_manager.get_fl_electrodes(
            electrode_groups=None
        )

    @should_raise(NoneParamInInitException)
    def test_manager_fails_creating_FlElectrodes_due_to_None_FlElectrodeGroup_attr(self):
        electrode_groups_metadata = [
            {'id': 0, 'location': 'mPFC', 'device_type': 'tetrode_12.5', 'description': 'Probe 1'},
            {'id': 1, 'location': 'mPFC', 'device_type': '128c-4s8mm6cm-20um-40um-sl', 'description': 'Probe 2'}]

        probes_metadata = [{'probe_type': 'tetrode_12.5', 'contact_size': 20.0, 'num_shanks': 1,
                            'shanks': [
                                {'shank_id': 0,
                                 'electrodes': [
                                     {'id': 0, 'rel_x': 0, 'rel_y': 0, 'rel_z': 0},
                                     {'id': 1, 'rel_x': 0, 'rel_y': 0, 'rel_z': 0},
                                     {'id': 2, 'rel_x': 0, 'rel_y': 0, 'rel_z': 0},
                                     {'id': 3, 'rel_x': 0, 'rel_y': 0, 'rel_z': 0}]}]},
                           {'probe_type': '128c-4s8mm6cm-20um-40um-sl', 'contact_size': 20.0, 'num_shanks': 4,
                            'shanks': [
                                {'shank_id': 0, 'electrodes': [
                                    {'id': 0, 'rel_x': 0, 'rel_y': 0, 'rel_z': 0},
                                    {'id': 1, 'rel_x': 40, 'rel_y': 0, 'rel_z': 0}]},
                                {'shank_id': 1, 'electrodes': [
                                    {'id': 32, 'rel_x': 0, 'rel_y': 300, 'rel_z': 0},
                                    {'id': 33, 'rel_x': 40, 'rel_y': 300, 'rel_z': 0}]},
                                {'shank_id': 2, 'electrodes': [
                                    {'id': 64, 'rel_x': 0, 'rel_y': 600, 'rel_z': 0},
                                    {'id': 65, 'rel_x': 40, 'rel_y': 600, 'rel_z': 0}, ]},
                                {'shank_id': 3, 'electrodes': [
                                    {'id': 96, 'rel_x': 0, 'rel_y': 900, 'rel_z': 0},
                                    {'id': 97, 'rel_x': 40, 'rel_y': 900, 'rel_z': 0}]}]}
                           ]

        mock_eg_1 = Mock()
        mock_eg_2 = Mock()
        mock_eg_1.__class__ = FLElectrodeGroup
        mock_eg_2.__class__ = FLElectrodeGroup
        mock_eg_1.name = None
        mock_eg_2.name = 'FLElectrodeGroup2'

        fl_electrodes_manager = FlElectrodeManager(probes_metadata, electrode_groups_metadata)

        fl_electrodes_manager.get_fl_electrodes(
            electrode_groups=[mock_eg_1, mock_eg_2]
        )