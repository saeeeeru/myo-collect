import os, argparse, time, sys

import myo
import numpy as np

# setting paramters
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('-T', '--terminate_time', type=int, default=60, help='terminate time[s]')
parser.add_argument('-n', '--index', type=int, help='index number of sample')
parser.add_argument('-D', '--dataset', type=str, default='tennis', help='dataset name')
args = parser.parse_args()

print('\nThis sample index: {0}'.format(args.index))
# print('This program will terminate in {0} seconds\n'.format(args.terminate_time))

# setting directory for output
outdir = os.path.join('.',args.dataset,'_dat')
if not os.path.exists(outdir):
	os.makedirs(outdir)

def convert_tolist(data):
	return [data.x, data.y, data.z]

class Listener(myo.DeviceListener):
	def __init__(self):
		self.datadict = {'acc':[],'gyro':[],'emg':[]}
		self.start_time = time.time()

	def on_connected(self, event):
		print("Hello, {0}!".format(event.device_name))
		event.device.vibrate(myo.VibrationType.short)
		event.device.stream_emg(True)

	def on_disconnevt(self, event):
		print('Bye, bye!')

	def on_orientation(self, event):
		self.datadict['acc'].append(convert_tolist(event.acceleration))
		self.datadict['gyro'].append(convert_tolist(event.gyroscope))
		
		sys.stdout.write('\relapsed time:{0}'.format(time.time()-self.start_time))
		sys.stdout.flush()

	def on_emg(self, event):
		self.datadict['emg'].append(event.emg)

if __name__ == '__main__':

	myo.init(sdk_path='')  # please insert the sdk file path
	hub = myo.Hub()
	listener = Listener()

	try:
		while hub.run(listener.on_event, 100):
			pass
	except KeyboardInterrupt:
		print("\nQuiting ...")
		hub.stop()

		for key, item in listener.datadict.items():
			np.savetxt(fname=os.path.join(outdir,key+'-'+str(args.index)+'.csv'),X=np.array(item), delimiter=',')
