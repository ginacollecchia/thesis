windowsmooth <- function (windows=5, data) {
	# padd vector at two ends
	pd <- data # vector to find average of a window of the data, size = 2*windows
	for (i in 1:windows) {pd <- c(data[1], pd)}				# pad length of windows from the beginning of the data
	for (i in 1:windows) {pd <- c(pd, data[length(data)])}		# pad length of windows at the end of the data
	
	# create smoothed vector
	sd <- data
 	for (i in 1:length(data)) {sd[i] <- mean(pd[i:(i+windows+windows)])}
	sd
}

# read the data
ohd = read.table('~/Desktop/metroid.csv')
# convert to a matrix
ohdm=as.matrix(ohd)

# next two lines plot a contour and note labels
# variables: 32 (number of frames to smooth), nlevels is the number of contours
notes=c("C","C#","D","D#","E","F","F#","G","G#","A","A#","B")
filled.contour(windowsmooth(32,ohdm), color.palette=topo.colors, asp=0.5, axes=FALSE, frame.plot=FALSE, nlevels=50)
axis(2, at=(0:11)/11, labels=notes)
powers <- function (frames) {
	c(sum(frames[,1]),sum(frames[,2]),sum(frames[,3]),sum(frames[,4]),sum(frames[,5]),sum(frames[,6]),sum(frames[,7]),sum(frames[,8]),sum(frames[,9]),sum(frames[,10]),sum(frames[,11]),sum(frames[,12]))
}
notepowers <- function(frames){data.frame(name=notes,power=powers(ohdm))}
# notepowers(ohdm) will give you a table of notes and their powers
ohdp=notepowers(ohdm)
# this gives a list of the top 7 most powerful note names
ohdp$name[order(ohdp$power, decreasing=TRUE)][1:7]