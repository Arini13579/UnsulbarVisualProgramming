
class A:
   def __init__(diri, nama, umur):
      diri.nama = nama       # public
      diri.__umur = umur  # private

   def who(diri):
      print('Nama  : ', diri.nama)
      print('umur : ', diri.__umur)