import File_Filter



File_Filter.SetDemandInfo("../testfile/DemandInfo.txt")
File_Filter.SetUserInfo("../testfile/UserInfo.txt")
File_Filter.SetKeyWords("../testfile/KeyWords.txt")
File_Filter.SetFile("../testfile/Files/test_1.txt")
File_Filter.SetFile("../testfile/Files/test_2.txt")
File_Filter.SetFile("../testfile/Files/test_3.txt")
Begin_dic = File_Filter.Begin()
# Flag = False
# while Flag == False:
#     Flag = File_Filter.Run(Begin_dic)
# File_Filter.End()