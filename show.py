while (( (globals().update({"i": 0}) or globals().update({"s": input()}) or print(globals().get("s"))) if globals().get("l") == None else None) or globals().get("s")) != globals().get("l") and globals().get("i") < 25: a = ( globals().update({"l": (globals().get("s"))}) or globals().update({"s": (''.join(['1' if globals().get("s")[0] == '1' else '']+[('0' if (n != 0 and n!=(len(globals().get("s"))-1) and (globals().get("s")[n-1:n+2] == '000' or globals().get("s")[n-1:n+2] == '100' or globals().get("s")[n-1:n+2] == '111') ) else '0' if (n == (len(globals().get("s"))-1) and ( ((globals().get("s")[-2] if len(globals().get("s"))>1 else '0')+globals().get("s")[-1]) == '00' or ((globals().get("s")[-2] if len(globals().get("s"))>1 else '0')+globals().get("s")[-1]) == '10') ) else '0'  if (n == 0 and globals().get("s")[0]+(globals().get("s")[1] if len(globals().get("s"))>1 else '0') == '00'  ) else '1') for n in range(0,len(globals().get("s")))]) )})  or (print(globals().get("s")) if globals().get("s") != globals().get("l") else None) or (globals().update({"i": globals().get("i")+1})) or 1)
