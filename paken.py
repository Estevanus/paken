import time
import sqlite3

debugValue = False

huruf = "abcdefghijklmnopqrstuvwxyz "
angka = "0123456789"
simbol = """`~!@#$%^&*()_+[]\{}|;'":,./<>?"""


sumber = []
for i in huruf:
	sumber.append(i)
for i in huruf.upper():
	sumber.append(i)
for i in angka:
	sumber.append(i)
for i in simbol:
	sumber.append(i)
	

c = sqlite3.connect("data.oscdb")


patokan = 531441
class digit:
	def __init__(self, isi, parent):
		self.isi = isi
		self.parent = parent
		self.awal = False
		self.akhir = False
		self.sebelumnya = None
		self.selanjutnya = None
		self.index = 0
		self.done = False
		
	def loop(self):
		for i in self.isi:
			if self.parent.dapat == True:
				break
			if self.selanjutnya != None:
				self.selanjutnya.done = False
				self.selanjutnya.loop()
			self.parent.scanned[self.index] = i
			if self.akhir == True:
				self.parent.totalScanned += 1
				if self.parent.callback(''.join(self.parent.scanned)) == True:
					#print("password didapati pada putaran ke {0} :3".format(str(self.parent.totalScanned)))
					print("pasddword didapati")
					self.parent.dapat = True
					self.parent.hasil = ''.join(self.parent.scanned)
				if debugValue == True:
					print(self.parent.scanned)
		if self.parent.firstLoop == True and self.akhir == True and self.parent.totalScanned > patokan:
			self.parent.firstLoop = False
			wa = time.time() - self.parent.t
			#wa = 23
			print("waktu yang dibutuhkan di saat awal ialah " + str(wa))
			perkiraanSelesai = self.parent.totalLoop / patokan * wa
			#print(wa)
			if perkiraanSelesai < 60:
				print("perkiraan selesai ialah " + str(perkiraanSelesai) + " detik")
			else:
				if perkiraanSelesai < 3600:
					menit = int(perkiraanSelesai / 60)
					detik = (perkiraanSelesai / 60 - menit) * 60
					print("perkiraan selesai ialah {0} menit dan {1} detik".format(str(menit), str(detik)))
				else:
					jam = perkiraanSelesai / 3600
					menit = (jam - int(jam)) * 60
					detik = (menit - int(menit)) * 60
					jam = int(jam)
					menit = int(menit)
					print("perkiraan selesai ialah {2} jam, {0} menit, dan {1} detik".format(str(menit), str(detik), str(jam)))
		self.done = True
				
				
		
	def __repr__(self):
		return "<class digit>" + str(isi)
		
class utama:
	def __init__(self):
		self.scanned = []
		self.totalScanned = 0
		self.firstLoop = True
		self.totalLoop = 0
		self.dapat = False
		self.t = time.time()
		self.callback = None
		self.hasil = ""
		

def scan(maxDigit, callback):
	digits = []
	awal = None
	seb = None
	u = utama()
	u.callback = callback
	for i in range(maxDigit):
		u.scanned.append("")
		dg = digit(sumber, u)
		dg.index = i
		if seb != None:
			dg.sebelumnya = seb
			seb.selanjutnya = dg
		else:
			dg.awal = True
			awal = dg
		seb = dg
		digits.append(dg)
	dg.akhir = True
	t = time.time()
	totalLoop = len(sumber) ** maxDigit
	u.totalLoop = totalLoop
	print("total loop ialah " + str(totalLoop))
	awal.loop()
	waktuSelesai = time.time() - t
	print("waktu selesai ialah " + str(waktuSelesai))
	print("pada putaran " + str(u.totalScanned) + " dari " + str(totalLoop) + " putaran")
	if u.dapat == True:
		return u.hasil
	else:
		return False