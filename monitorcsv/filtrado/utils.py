def epoch_to_string(numero):
    import time
    print numero
    print type(numero)
    resultado = time.strftime('%m/%d/%Y %H:%M:%S', time.gmtime(float(numero)))
    return resultado
#    time.struct_time(tm_year=2017, tm_mon=8, tm_mday=20, tm_hour=20, tm_min=55, tm_sec=2, tm_wday=6, tm_yday=232, tm_isdst=0)

