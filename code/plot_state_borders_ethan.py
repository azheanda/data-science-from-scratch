import urllib
from xml.dom import minidom
from matplotlib import pyplot as plt

def plot_state_borders(plt, color='0.8'):
    url = 'http://econym.org.uk/gmap/states.xml'
    xml = urllib.urlopen(url).read()
    xmldoc = minidom.parseString(xml)
    lineSegments = []

    stateNodes = xmldoc.getElementsByTagName('state')
    for stateNode in stateNodes:
    	pointNodes = stateNode.getElementsByTagName('point')
    	num_points = len(pointNodes)
    	for i in xrange(num_points):
    		p1 = pointNodes[i];
    		p2 = pointNodes[(i+1) % num_points]
    		lineSegments.append(zip(get_lat_lng(p1), get_lat_lng(p2)))

    for line in lineSegments:
        plt.plot(*line, color='r')



def get_lat_lng(point):
	return [point.getAttribute('lng'), point.getAttribute('lat')]