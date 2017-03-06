import os
import json
from shutil import copyfile

RESULTS_PATH = ''

def msd_id_to_dirs(msd_id):
	"""Given an MSD ID, generate the path prefix. E.g. TRABCD12345678 -> A/B/C/TRABCD12345678"""
	return os.path.join(msd_id[2], msd_id[3], msd_id[4], msd_id)

def msd_id_to_h5(msd_id):
	"""Given an MSD ID, return the path to the corresponding h5"""
	return os.path.join(RESULTS_PATH, 'lmd_matched_h5', msd_id_to_dirs(msd_id).strip('\n') + '.h5')

def get_midi_path(msd_id, midi_md5, kind):
	"""Given an MSD ID and MIDI MD5, return path to a MIDI file. kind vshould be one of 'matched' or 'aligned'. """
	return os.path.join(RESULTS_PATH, 'lmd_{}'.format(kind), msd_id_to_dirs(msd_id).strip('\n'), midi_md5 + '.mid')

# Load JSON into dict
with open('match_scores.json') as f:
    scores = json.load(f)

tracks = open('electronic_tracks.txt','r')
for track in tracks.xreadlines():
	matches = []
	try:
		matches = scores[track.strip('\n')].items()
	except KeyError:
		pass

	for midi_md5 in matches:
		path = get_midi_path(track, midi_md5[0], 'matched')
		try:
			dst = 'electronic/' + track.strip('\n') + '.mid'
			copyfile(path, dst)
		except IOError:
			pass
