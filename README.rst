Overview
========

The qrlogo project allows you to build arbitrarily large QR codes with a logo overlaid on a region of it.  The QR code is converted to a PNG file and you can save it by right-clicking and selecting 'Save Image As'.

Example Output
==============

.. image:: qrlogo/output_example.png

Here is the URL used to generate the above example::

index.html?logo=http://www.ces.ncsu.edu/plymouth/ent/pics/ncsu_logo_1.gif&qr_w=500&qr_h=500&logo_w=100&logo_h=100&logo_x_offset=300&logo_y_offset=300&text=www.ncsu.edu&/

Usage
=====

index.html respects these GET Parameters:

qr_w
  the width of the QR code generated in pixels
qr_h
  the height of the QR code generated in pixels

logo 
  the URL of the logo to overlay on top of the QR code
logo_w
  The width of the overlaid logo in pixels
logo_h
  The height of the overlaid logo in pixels

text
  The URL (or plaintext) that the QR code should resolve to.  This is typically a URL (ie: http://www.ncsu.edu)
