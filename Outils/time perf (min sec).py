minu = round((time.perf_counter()/60),2)
seco = (minu - int (minu) ) * 60
print('(en', int(minu),'\rmin et', int(seco), '\rsec)')