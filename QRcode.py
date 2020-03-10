#QRcode genrate and testing By ijaz sial Github    PakBulelt
# Import QRCode from pyqrcode 
import pyqrcode 
from pyqrcode import QRCode 
  
  
# String which represent the QR code 
s = "https://github.com/PakBullet"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("PakBulletQRcode.svg", scale = 8)