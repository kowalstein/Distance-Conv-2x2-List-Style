L = [[1, 12, 0.333, 0.000187, 304.8, 30.48, 0.3048, 0.000304],
		[0.0833, 1, 0.278, 1.578*10**-5, 25.4, 2.54, 0.0254, 2.54*10**-5],
		[3, 36, 1, 0.000568, 914.4, 91.44, 0.914, 0.000914],
		[5280, 63360, 1760, 1, 1609344, 160934.4, 1609.344, 1.609],
		[0.00328084, 0.0394, 0.00109, 6.214*10**-7, 1, 0.1, 0.001, 1*10**-6],
		[0.0328084, 0.394, 0.0109, 6.214*10**-6, 10, 1, 0.01, 1*10**-5],
		[3.28084, 39.37, 1.094, 0.000621, 1000, 100, 1, 0.001],
		[3280.84, 39370.079, 1093.613, 0.621, 1*10**15, 100000, 1000, 1]]
units = ['ft', 'in', 'yd', 'mi', 'mm', 'cm', 'm', 'km']
print (' CONVERSION KEY:')
print (' [FEET = 1] [INCHES = 2] [YARDS = 3] [MILES = 4]')
print (' [MILLIMETERS = 5] [CENTIMETERS = 6]')
print (' [METERS = 7] [KILOMETERS = 8]')
print ()
num = eval( input( ' Enter the number you want to convert: '))
fro = eval( input( ' What unit are you converting from: '))
to = eval( input( ' What unit are you converting to:'))
flag = 0
for r in range (8):
	for c in range (8):
		if fro == r+1 and to == c+1:
			flag = 1
			ans = num*L[r][c]
			unit1 = units[r]
			unit2 = units[c]
if flag == 1:
	print ()
	print (' '+str(num)+unit1+' has been converted to '+str(ans)+unit2)
else:
	print ()
	print ('INVALID SELECTIONS!!!')
