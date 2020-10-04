def jpeg_res(filename):
   "Prints the resolution of the jpeg image file passed into it"

   with open(filename,'rb') as img_file:

       img_file.seek(163)

       a = img_file.read(2)

       # calculate height
       height = (a[0] << 8) + a[1]

       a = img_file.read(2)

       # calculate width
       width = (a[0] << 8) + a[1]

   print("\nThe resolution of the image is",width,"x",height)

filename = input('\nInput jpeg image filename: ')
jpeg_res("images/"+filename)
