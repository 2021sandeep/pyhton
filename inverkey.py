def Invert_key_and_values(dicti):
  dicti_temp=dict()
  for key, value in dicti.items():
    dicti_temp[value]=key
  return dicti_temp
print(Invert_key_and_values({"a":"b","c":"d"}))
