#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import cv2
from PIL import Image
import numpy as np
import rospy
import matplotlib.pyplot as plt
from facenet_pytorch import InceptionResnetV1
from facenet_pytorch import MTCNN
from carry_food_v2.msg import PositionValues
from collections.abc import Mapping
from std_msgs.msg import String


class capface():

    def __init__(self):
        """
        ノードの作成
        出版者の作成
        """
        rospy.init_node("face")
        self.face_pub = rospy.Publisher("/face", PositionValues, queue_size=1)
        self.audio_pub = rospy.Publisher("/audio", String, queue_size=1)
        #elf.a = 0

        # self.face_pub = 0

        print("初期化")


    #1つ目の関数
    def get_face(self):

        mtcnn = MTCNN() #MTCNNモデルを取得する
        # カメラの読込み
        # 内蔵カメラがある場合、下記引数の数字を変更する必要あり
        cam_num = 0
        try:
            cap = cv2.VideoCapture(cam_num)
        except:
            cam_num += 1

        num = 0 #撮影枚数を保持する変数

        #print(self.a)



        left_ave = 0 #平均値
        up_ave = 0
        right_ave = 0
        down_ave = 0

        frame_count = 0 #一度だけフレームの大きさを取得するため

        ##ロボットから見た
        robo_face_dis = 0  #顔の距離
        robo_face_drct = 0 #顔の方向
        robo_face_hgt = 0  #顔の高さ

        # 動画終了 かつ 最大枚数を超えるまで まで、1フレームずつ読み込んで表示する。
        while(cap.isOpened()):

            ret, frame = cap.read()# 1フレーム毎　読込み

           

            # OpenCVでも入力できる
            # 顔領域、顔っぽさ、特徴点のリストを取得、顔が1つなら長さ1
            boxes, probs, points = mtcnn.detect(frame, landmarks=True)
            #print(boxes)        

            if boxes is not None:
                #imageCropped = mtcnn(image) # MTCNNで顔検出、切り取った160x160の画像を保存
                #int(boxes[0][0]), int(boxes[0][1])), (int(boxes[0][2]), int(boxes[0][3])
                #切り出し範囲＝img[縦方向（上）：縦方向（下）, 横方向（左）：横方向（右）]
                #左下、右上
                #dtcimage =cv2.rectangle(frame, (int(boxes[0][0]), int(boxes[0][1])), (int(boxes[0][2]), int(boxes[0][3])), color=(255, 0, 0), thickness=2)
                #cut_frame = frame[int(boxes[0][1]):int(boxes[0][3]), int(boxes[0][0]):int(boxes[0][2])] 

                #1回だけフレームの大きさを取得する
                if frame_count == 0:
                    frame_h, frame_w, _ = frame.shape
                    frame_count = 1

                #リストに値を追加し、幅、高さ、中心座標の平滑化を行う
                left = [] 
                up = []
                right = []
                down = []
               
                
                for i in range(20):
                    left.append(boxes[0][0])
                    up.append(boxes[0][1])
                    right.append(boxes[0][2])
                    down.append(boxes[0][3])

                    left_ave = int(sum(left)/len(left)) #平均値
                    up_ave = int(sum(up)/len(up))
                    right_ave = int(sum(right)/len(right))
                    down_ave = int(sum(down)/len(down))



                #time.sleep(WAIT_TIME) #顔が見つかったら1秒待つ
                cv2.rectangle(frame, (left_ave, up_ave), (right_ave, down_ave), (255, 0, 0))
                #cv2.imwrite(FOLDER + "/" + IMG + str(num) +  ".png", frame)

                #顔の矩形の幅
                w = int(right_ave - left_ave)
                h = int(down_ave - up_ave)

                #顔の矩形の位置
                c_x = int((right_ave + left_ave)/2)
                c_y = int((down_ave + up_ave)/2)



                #ロボットと顔との距離
                if w < frame_w/5:
                    robo_face_dis = 0

                elif w >= frame_w/5 and w <= frame_w/3:
                    robo_face_dis = 1

                elif w > frame_w/3:
                    robo_face_dis = 2



                #ロボットから見た顔の方向　
                if c_x < frame_h/3:
                    robo_face_drct = 0

                elif c_x >= frame_w/3 and c_x <= frame_w*2/3:
                    robo_face_drct = 1

                elif c_x > frame_w*2/3:
                    robo_face_drct = 2



                #ロボットから見た顔の高さ
                if c_y < frame_h/3:
                    robo_face_hgt = 0

                elif c_y >= frame_h/3 and c_y <= frame_h*2/3:
                    robo_face_hgt = 1

                elif c_y > frame_h*2/3:
                    robo_face_hgt = 2

        
            print("robo_face_dis=" + str(robo_face_dis))
            print("robo_face_drct=" + str(robo_face_drct))
            print("robo_face_hgt=" + str(robo_face_hgt))

            
            """
            顔との距離、方向、高さを出版する
            """   

            p = PositionValues()
            p.up_down = robo_face_hgt
            p.far_near = robo_face_dis
            p.left_right = robo_face_drct

            self.face_pub.publish(p)
             
            
            
            cv2.imshow('face_dtc' , frame)

            # qキーが押されたら途中終了
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # 終了処理
        cap.release()
        cv2.destroyAllWindows()


 

if __name__ == "__main__":
    cp = capface()
    cp.get_face()
    # インスタンス生成
    #human1 = Human()
    
    #uman1.printinfo()