windowsmooth <- function (ww=5, dd) {
	# padd vector at two ends
	pp <- dd
	for (i in 1:ww) {pp <- c(dd[1], pp)}				# padd start ww times
	for (i in 1:ww) {pp <- c(pp, dd[length(dd)])}		# padd end ww times
	
	# create smoothed vector
	ss <- dd
 	for (i in 1:length(dd)) {ss[i] <- mean(pp[i:(i+ww+ww)])}
	ss
}

# read the data
ohd = read.table('Desktop/ohd.csv')
# convert to a matrix
ohdm=as.matrix(ohd)

# next two lines plot a contour and note labels
# variables: 32 (number of frames to smooth), nlevels is the number of contours
filled.contour(windowsmooth(32,ohdm), color.palette=topo.colors, asp=0.5, axes=FALSE, frame.plot=FALSE, nlevels=50)
> axis(2, at=(0:11)/11, labels=notes, line=-2)
