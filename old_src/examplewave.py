import sys, os, wave, array
import numpy.fft

def read_wav_as_array(inputfile):
	"""takes as input a wav file, outputs a tuple of the data as an array and the params of the wav file as a list"""
	#Open the file
	aw = wave.open(inputfile,'r')
	#Figure out how long it is
	nframes = aw.getnframes()		#from "wave"; goolgle "python wave"
	#Read all of it as a string
	data= aw.readframes(nframes)
	#Convert this string to an array of pairs of 16bit integers -- so each item is [a,b] where -32768<a,b<32767 one sample per channel, 
	#unless of course your data is mono in which case it wont be a pair...
	data = array.array("h", data)
	params = aw.getparams()
	aw.close						#done with file, read into memory
	
	newdata = []
	for x in xrange(0,88200,2):		#2 seconds
		newdata.append(x)
	print len(newdata)
	for x in xrange(0,len(newdata),512):
		samplebit = numpy.fft.fft(newdata[x:x+512]).real
		samplebit = list(samplebit)
		print samplebit
		samplebit = [str(y) for y in samplebit]
		f = open(str(x)+'.txt','w')
		f.write('\n'.join(samplebit))
		f.close()
	

	return (data,params)
def write_vector_as_wav(data,name,pram):
	"""writes a wav file: data is an array (as in array.array()) of numerics, name is just a string,pram""" 
	aw = wave.open(name+'.wav','w')
	aw.setparams(pram)
	aw.writeframes(data.tostring())
	aw.close
def test(inputfile):
	a = read_wav_as_array(source)
	print a[1]
	print a[0][:5]
	write_vector_as_wav(a[0],'test.wav',a[1])


if __name__=="__main__":
	read_wav_as_array(sys.argv[1])