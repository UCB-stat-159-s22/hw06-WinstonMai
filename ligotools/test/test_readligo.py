from ligotools import readligo as rl
import numpy as np
import json

def test_strain_hdf5():
    strain, time, channel_dict = rl.loaddata('data/H-H1_LOSC_4_V2-1126259446-32.hdf5', 'H1')
    assert (len(strain) == 131072)

def test_time_hdf5():
    strain, time, channel_dict = rl.loaddata('data/H-H1_LOSC_4_V2-1126259446-32.hdf5', 'H1')
    assert (len(time) == 131072)

def test_cd_hdf5():
    strain, time, channel_dict = rl.loaddata('data/H-H1_LOSC_4_V2-1126259446-32.hdf5', 'H1')
    assert (len(channel_dict) == 13)

def test_dq2segs():
    strain, time, channel_dict = rl.loaddata('data/H-H1_LOSC_4_V2-1126259446-32.hdf5', 'H1')
    assert rl.dq2segs(channel_dict['CBC_CAT3'], 0).__class__ == rl.SegmentList
