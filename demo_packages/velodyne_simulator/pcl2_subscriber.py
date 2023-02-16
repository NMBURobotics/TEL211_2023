#!/usr/bin/env python

from matplotlib.pyplot import install_repl_displayhook
from sensor_msgs.msg import PointCloud2
import rospy
import ros_numpy
import random
import math

# Refer to for equations https://medium.com/@ajithraj_gangadharan/3d-ransac-algorithm-for-lidar-pcd-segmentation-315d2a51351 

class RANSAC:
    """
    RANSAC Class
    """
    def __init__(self, point_cloud, max_iterations, distance_ratio_threshold):
        self.point_cloud = point_cloud
        self.max_iterations = max_iterations
        self.distance_ratio_threshold = distance_ratio_threshold

    def ransac_algorithm(self):

        inliers_result = set()
        while self.max_iterations:
            self.max_iterations -= 1
            # Add 3 random indexes
            random.seed()
            inliers = []
            while len(inliers) < 3:
                random_index = random.randint(0, len(self.point_cloud)-1)
                inliers.append(random_index)
            # print(inliers)

            # In case of *.pcd data
            x1, y1, z1 = self.point_cloud[inliers[0]]
            x2, y2, z2 = self.point_cloud[inliers[1]]
            x3, y3, z3 = self.point_cloud[inliers[2]]
            # Plane Equation --> ax + by + cz + d = 0
            # Value of Constants for inlier plane
            a = (y2 - y1)*(z3 - z1) - (z2 - z1)*(y3 - y1)
            b = (z2 - z1)*(x3 - x1) - (x2 - x1)*(z3 - z1)
            c = (x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1)
            d = -(a*x1 + b*y1 + c*z1)
            plane_lenght = max(0.1, math.sqrt(a*a + b*b + c*c))

            for index, point in  enumerate(self.point_cloud):
                
                # Skip iteration if point matches the randomly generated inlier point
                if index in inliers:
                    continue

                x, y, z = point[0], point[1], point[2]

                # Calculate the distance of the point to the inlier plane
                distance = math.fabs(a*x + b*y + c*z + d)/plane_lenght
                # Add the point as inlier, if within the threshold distancec ratio
                if distance <= self.distance_ratio_threshold:
                    inliers.append(index)
            # Update the set for retaining the maximum number of inlier points
            if len(inliers) > len(inliers_result):
                inliers_result= set()
                inliers_result = inliers

        # Segregate inliers and outliers from the point cloud
        inlier_points = []
        outlier_points = []
        for index, point in  enumerate(self.point_cloud):
            if index in inliers_result:
                inlier_points.append(point)
                continue
            outlier_points.append(point)

        return inlier_points, outlier_points

class PointCloudSubscriberNode():
    
    def __init__(self, *args):
        print("Constructing PointCloudSubscriberNode")
        self.pointcloud_subscriber = rospy.Subscriber("/velodyne_points", PointCloud2, self.callback,queue_size=1,buff_size=2002428800)
    
    def callback(self, msg):
        xyz_array = ros_numpy.point_cloud2.pointcloud2_to_xyz_array(msg)
        ransac = RANSAC(xyz_array, max_iterations=10, distance_ratio_threshold=0.1)
        inlier, outlier = ransac.ransac_algorithm()
        print("I have recieved a Pointcloud with message: ", len(xyz_array), len(inlier), len(outlier))
        
if __name__ == '__main__':
    node = PointCloudSubscriberNode()
    rospy.init_node('PointCloudSubscriberNode', anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        rate.sleep()
    print("Shutting down PointCloudSubscriberNode")
        
        