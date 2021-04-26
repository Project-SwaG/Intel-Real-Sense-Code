# -*- encoding: utf-8 -*-
"""
 @File: test_191123_Print the depth map as a black and white image.py
@Time    : 2019/11/24 15:57
@Author  : Dontla
@Email   : sxana@qq.com
@Software: PyCharm
"""
import pyrealsense2 as rs
import cv2 as cv
import numpy as np

pipeline = rs.pipeline()

cfg = rs.config()
cfg.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
cfg.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

profile = pipeline.start(cfg)

try:
    while True:
        fs = pipeline.wait_for_frames()

        color_frame = fs.get_color_frame()
        depth_frame = fs.get_depth_frame()

        if not depth_frame or not color_frame:
            continue

        color_image = np.asanyarray(color_frame.get_data())
        depth_image = np.asanyarray(depth_frame.get_data())

        # Print in black and white
        # depth_image = cv.convertScaleAbs(depth_image, alpha=0.03)
        # Print in color
        # depth_image = cv.applyColorMap(cv.convertScaleAbs(depth_image, alpha=0.03), cv.COLORMAP_JET)

        # Test whether you can map CV_24UC3
        color_image = cv.applyColorMap(color_image, cv.COLORMAP_JET)

        window = cv.namedWindow('window', cv.WINDOW_AUTOSIZE)

        cv.imshow('window', color_image)

        cv.waitKey(1)
finally:
    pipeline.stop()

