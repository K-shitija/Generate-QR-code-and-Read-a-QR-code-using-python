# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 17:08:29 2023

@author: KSHITIJA
"""

#Generating a Simple QR Code and pass data

import qrcode
#create object for QRCode
obj_qr =qrcode.QRCode(
        version=1,
        error_correction =qrcode.constants.ERROR_CORRECT_L,
        box_size =10,
        border =4,
        )
#using the add_data() function
obj_qr.add_data("https://github.com/K-shitija")
#use make() function
obj_qr.make(fit=True)
#using make_image() function
qr_img = obj_qr.make_image(fill_color = 'white',back_color = "green")


#save image file
qr_img.save("qr-img.jpg")

#Read QR code

#make qr code
qr_code = qrcode.make("Welcome to my QRcode -Regards Kshitija")
qr_code.save("my_first_QR.jpg")

import cv2
qr_img=cv2.imread("F:\Python_project_persoanl\Project_Files\QR_code_scanner\my_first_QR.jpg")   #read image
qr_dectect = cv2.QRCodeDetector()  #detectQRcode
val,pts,st_code = qr_dectect.detectAndDecode(qr_img)
print("Information: ",val)



