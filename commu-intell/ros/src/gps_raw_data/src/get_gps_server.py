import rospy
from gps_raw_data.srv import gps_srv, gps_srvResponse
from gps_raw_data import readLatLng

def handle_requests():
    coordinates = readLatLng()
    return gps_srvResponse(coordinates[0], coordinates[1])

def get_gps_server():
    rospy.init_node('get_gps_server')
    s = rospy.Service('get_gps_server', gps_srv, handle_requests)
    rospy.spin()

if __name__ == "__main__":
    get_gps_server()