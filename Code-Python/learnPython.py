print("^-^ Web Phim HackLong Dev ^-^")
print("Vui lòng tra khảo tuổi để lựa phim như sau:")
age = input("Nhập tuổi: ")
if age < str(18):
     print("Ko nên xem trang web phim này")
     print("Vui lòng đợi đủ 18 tuổi và quay trở lại ^_^")
elif age < str(30):
     print("Phim lành mạnh cho thanh niên 18+")
     print("Vui lòng ấn vào đây để xem phim cho thanh niên mới lớn:)")
elif age < str(70):
     print("Phim lành mạnh cho người lớn")
     print("Vui lòng ấn vào đây để xem phim cho người lớn:)")
else:
     print("Phim lành mạnh cho người già")
     print("Vui lòng ấn vào đây để xem phim cho người già:)")
print("^_^ Web phim HackLong Dev xin trân trọng phục vụ ^_^")
