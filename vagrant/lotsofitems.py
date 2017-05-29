from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Computer, ComputerParts
engine = create_engine('sqlite:///partsdata.db')
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()

#Parts list for Category 1
computer1 = Computer(name="Solid State Drives")

session.add(computer1)
session.commit()

computerParts1 = ComputerParts(name='SAMSUNG 850 2.5', description='250GB SATA III Vertical Internal Solid State Drive', price='$109.99', computer=computer1)

session.add(computerParts1)
session.commit()

computerParts2 = ComputerParts(name = "Crucial MX300 2.5", description = "525GB SATA III Vertical Internal Solid State Drive", price = "$159.99", computer=computer1)

session.add(computerParts2)
session.commit()

computerParts3 = ComputerParts(name = "ADATA Ultimate SU800", description="256GB SATA III Internal Solid State Drive", price = "$99.99", computer=computer1)

session.add(computerParts3)
session.commit()

#Parts list for Category 2
computer2 = Computer(name = "Graphics Cards")

session.add(computer2)
session.commit()


computerParts1 = ComputerParts(name = "EVGA GeForce GTX 1080", description = "FTW GAMING ACX 3.0, 08G-P4-6286-KR, 8GB GDDR5X, RGB LED, 10CM FAN, 10 Power Phases, Double BIOS, DX12 OSD Support (PXOC)", price = "$559.99", computer=computer2)

session.add(computerParts1)
session.commit()

computerParts2 = ComputerParts(name = "MSI GeForce GTX 1070", description = "GAMING X 8G 8GB 256-Bit GDDR5 PCI Express", price = "$404.99", computer=computer2)

session.add(computerParts2)
session.commit()

computerParts3 = ComputerParts(name = "ASUS ROG GeForce GTX 1070", description = "8GB 256-Bit GDDR5 PCI Express 3.0 HDCP Ready Video Card with RGB Lighting", price = "$449.99", computer=computer2)

session.add(computerParts3)
session.commit()


#Menu for Panda Garden
computer3 = Computer(name = "Power Source")

session.add(computer3)
session.commit()


computerParts1 = ComputerParts(name = "CORSAIR RMx Series RM750X 750W", description = "80 PLUS GOLD Haswell Ready Full Modular ATX12V & EPS12V SLI and Crossfire Ready Power Supply", price = "$99.99", computer=computer3)

session.add(computerParts1)
session.commit()

computerParts2 = ComputerParts(name = "EVGA SuperNOVA 750 G1 120-G1-0750-XR ", description = "80+ GOLD 750W Fully Modular Includes FREE Power On Self Tester Power Supply", price = "$99.99", computer=computer3)

session.add(computerParts2)
session.commit()

computerParts3 = ComputerParts(name = "SeaSonic SSR-650RM 650W ATX12V", description = "EPS12V SLI Ready CrossFire Ready 80 PLUS GOLD Certified Modular Active PFC Power Supply New 4th Gen CPU", price = "$79.90", computer=computer3)

session.add(computerParts3)
session.commit()



print "added computer parts!"
