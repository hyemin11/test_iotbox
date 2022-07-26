# 각 농장 마다의 고유 데이터를 정의한 파일

FarmCode = 10

def MakeDevID(sensor_no):
    dev_id = '000-%05d-%04d' % (FarmCode, sensor_no)
    return dev_id

def Devid2No(dev_id):
    sensor_no = dev_id.split('-')
    sensor_no = int(sensor_no[2])
    return sensor_no
