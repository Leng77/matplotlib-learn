d={"a":24,"g":52,"i":12,"k":33}
print({k:v for k,v in sorted(d.items(),key=lambda x:x[1],reverse=False)})