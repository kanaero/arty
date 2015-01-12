import django
django.setup()

from operations.models import *

company_names = [
'AL AREEB',
'AL BARRAK',
'AL SAMIM',
'BMA',
'CAPITAL ONE',
'CNS LOGISTICS',
'COPIER INTERNATIONAL',
'DAMCO',
'DANZAS',
'DUCON',
'EVER SAFE SHIPPING',
'GAC LOGISTICS',
'INCHCAPE SHIPPING',
'INTERNATIONAL SHIPPING',
'LANDMARK',
'LG',
'MODERN FREIGHT',
'NMT International FZ Co',
'PANTOS',
'PRO GLOBAL LOGISTICS',
'QATAR NAVIGATION',
'RHS',
'SABA SHIPPING',
'SHIPPING SOLUTION',
'STEINWIG SHARAF',
'TIME WORLD FREIGHT',
'TRUEBELL INTL',
'WALLS & FLOORS',
'WHITEWAY SHIPPING',
'WIDE WING SHIPPING',
'WINNERS MARINE'
]

locations = [
'TTL',
'W/H 04',
'THAKRAL',
'THAKRAL',
'W/H 04',
'THAKRAL',
'CNS LOGISTICS',
'W/H 04',
'W/H 04',
'W/H 04',
'W/H 04',
'W/H 04',
'W/H 04',
'DUCON',
'LG NEW W/H',
'LG NEW W/H',
'DLC-1/KRYTON',
'FMCG',
'DLC-1/HUAWEI',
'QATAR NAVIGATION',
'APTEC GULF/DLC-3M',
'W/H 04',
'W/H 04',
'W/H 04',
'QATAR NAVIGATION',
'DLC-1/HUAWEI',
'DLC-1/HUAWEI',
'DLC-1/HUAWEI',
'QATAR NAVIGATION',
'THAKRAL',
'THAKRAL',
'THAKRAL',
'EXIDE',
'COPIER /IML',
'DLC-2/ANDREW',
'FMCG',
'FMCG',
'FMCG',
'FMCG',
'LG NEW W/H',
'LG NEW W/H',
'PURE FOOD',
'EXIDE',
'SIAFA PERFUMES',
'AL SAMIM',
'AL SAMIM',
'AL SAMIM',
'SAIFZONE',
'W/H 04',
'W/H 04',
'W/H 04',
'W/H 04',
'W/H 04',
'W/H 04',
'W/H 04',
'W/H 04',
'W/H 04',
'W/H 04',
'W/H 04',
'SMU',
'EXIDE',
'EXIDE',
'VC06/BLUESHED ',
'DLC-3/HYUNDAI',
'DLC-3/HYUNDAI',
'DLC-3/HYUNDAI',
'DLC-3/HYUNDAI',
'THAKRAL',
'THAKRAL',
'EXIDE',
'EXIDE',
'AIRLINK',
'SIAFA PERFUMES',
'SABRINE',
'SABRINE',
'SABRINE',
'SABRINE',
'ARAY GULF',
'ARAY GULF',
'DLC-3M',
'DLC-1/TYCO',
'ABLE ',
'ABLE ',
'ABLE ',
'ABLE ',
'ABLE ',
'ABLE ',
'ABLE ',
'ABLE ',
'ABLE ',
'ABLE ',
'ABLE ',
'SPECIAL TRADING',
'FMCG',
'FMCG',
'FMCG',
'AL SAYEGH',
'AL SAYEGH',
'LG NEW W/H',
'LG NEW W/H',
'LG NEW W/H',
'LG NEW W/H',
'QATAR NAVIGATION',
'AL SAMIM',
'AL SAMIM',
'BMA',
'BMA',
'W/H 04',
'W/H 04',
'W/H 04',
'W/H 04',
'W/H 04',
'W/H 04',
'W/H 04',
'W/H 04',
'W/H 04',
'W/H 04',
'FMCG',
'FMCG',
'APTECH GULF',
'DLC-3M',
'DLC-1/HUAWEI',
'DLC-1/HUAWEI',
'DLC-1/HUAWEI',
'DLC-1/HUAWEI',
'DLC-1/HUAWEI',
'DLC-1/HUAWEI',
'DLC-1/HUAWEI',
'DLC-1/HUAWEI',
'DLC-3M',
'ARAY GULF',
'ARAY GULF',
'BMA',
'THAKRAL',
'AL SAMIM',
'SABRINE',
'SABRINE',
'SABRINE',
'SABRINE',
'SABRINE',
'SABRINE',
'SABRINE',
'AL SAYEGH',
'FMCG',
]
locations = list(set(locations))

trucks = [
'27201',
'37771',
'38912',
'46065',
'46066',
'53309',
'54018',
'61252',
'61253',
'76299',
'76300',
'81503',
'81915',
'82641',
'91707',
'95750',
'96086',
'96230',
'96617',
'96677',
'96795',
'96799',
]
trucks = list(set(trucks))

drivers = [
'Abbas',
'Amrit',
'Avtar',
'Baljinder',
'Chamkur',
'Gurpreet',
'Jawad',
'Kannan',
'Madhav',
'Mandeep',
'Mazahir',
'Murugasan',
'Nishad',
'Pandian',
'Param',
'Prabhjot',
'Rafiq',
'Raja',
'Ranjith',
'Sarabjith',
'Sreekumar',
'Tilak',
'Thangavel',
'Zaheer',
'Zahid',
]
drivers = list(set(drivers))

assigned_truck=[
(27201,'Abbas'),
(37771,'Amrit'),
(38912,'Avtar'),
(46065,'Baljinder'),
(46066,'Chamkur'),
(53309,'Gurpreet'),
(54018,'Jawad'),
(61252,'Kannan'),
(61253,'Madhav'),
(76299,'Mandeep'),
(76300,'Mazahir'),
(81503,'Murugasan'),
(81915,'Nishad'),
(82641,'Pandian'),
(91707,'Param'),
(95750,'Prabhjot'),
(96086,'Rafiq'),
(96230,'Raja'),
(96617,'Ranjith'),
(96677,'Sarabjith'),
(96795,'Sreekumar'),
(96799,'Tilak')
]


# delete all objects
for x in [Customer,Location,Truck,Driver]:
	x.objects.all().delete()

for x in company_names:
	s = Customer(name=x)
	s.save()

for x in locations:
	o = Location(name=x)
	o.save()

for x in trucks:
	o = Truck(license_plate = x)
	o.save()

for x in drivers:
	o = Driver(first_name=x)
	o.save()

for (plate,name) in assigned_truck:
	truck = Truck.objects.get(license_plate=plate)
	driver = Driver.objects.get(first_name = name)
	truck.assigned_driver = driver
	truck.save()