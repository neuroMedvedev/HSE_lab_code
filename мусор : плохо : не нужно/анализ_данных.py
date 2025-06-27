import mne #eeg analysis
import numpy as np # dataframes and staff
import matplotlib.pyplot as plt # plots
import matplotlib # plots
import PyQt5 # how plots open in you PC
from pathlib import Path # path to files
from mne.channels import find_ch_adjacency # connection btw electrodes
from functools import partial # statistics
import scipy.stats #statistics
import pickle # way to save data
import seaborn as sns # data and stats
from scipy import stats # stats
import statistics # stats
import mne_qt_browser

#mne.viz.set_browser_backend('qt')

raw = mne.io.read_raw_brainvision('/Users/alexmedvedev/Desktop/ИКН ВШЭ/эксп/препилот кирил/school_kiril.vhdr', eog=['HEOG', 'VEOG'], misc = ['BIP1'], preload = True)

raw.info

montage = mne.channels.make_standard_montage("standard_1020")

raw.set_montage(montage)

#raw.plot_sensors(show_names = True)

raw.notch_filter(50)
raw.filter(1,45)

#ica.plot_sources(raw)

#ica.plot_components()

raw.plot(duration = 100)

events, ids = mne.events_from_annotations(raw)

dis_ids = {'5-6': 5 or 51, '7-8': 7 or 71, '9-10': 9 or 91, '11-12': 11 or 111}

five_id = {'5-6': 5 or 51}

dis_events = mne.pick_events(events, include = [5, 51, 7, 71, 9, 91, 11, 111])

mne.viz.plot_events(dis_events, event_id = dis_ids, sfreq = raw.info['sfreq'])

epochs_dis = mne.Epochs(raw, dis_events, dis_ids, tmin = -0.5, tmax = 1, baseline = (-0.5, 0), reject_by_annotation=True)

evoked_dis = epochs_dis.average()

evoked_dis.plot()

five_events = mne.pick_events(events, include = [5, 51])

epochs_five = mne.Epochs(raw, five_events, five_id, tmin = -0.5, tmax = 1, baseline = (-0.5, 0), reject_by_annotation=True)

evoked_five = epochs_five.average()

evoked_five.plot()