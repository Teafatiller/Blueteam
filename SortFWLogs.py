import re, argparse
parser = argparse.ArgumentParser()
parser.add_argument('-e','--exclude')
args = parser.parse_args()
if args.exclude: exclude = str(args.exclude)#last 4 lines r for args
ipv4 = '\d+\.\d+\.\d+\.\d+'
ipv6 = '[a-fA-F0-9]+\::[a-fA-F0-9:]+'
src, dst = [],[]
srcF, dstF = {},{}
with open(‘C:\\Users\\Administrator\Desktop\fwlogs.txt’, 'r') as f: #read log file
    log = f.read()
tmp = re.findall(ipv4, log)                 #parse for IPs
tmp += re.findall(ipv6, log)
for each in range(len(tmp)):                #create src and dst lists
    if each%2 == 0 : src.append(tmp[each])
    else : dst.append(tmp[each])
for i in src:                               #calc src IP freqs
    if i in srcF: srcF[i] += 1
    else: srcF[i] = 1
for i in dst:                               #calc dst IP freqs
    if i in dstF: dstF[i] += 1
    else: dstF[i] = 1
sortSrc = dict(sorted(srcF.items(), key=lambda x: x[1], reverse=True))
sortDst = dict(sorted(dstF.items(), key=lambda x: x[1], reverse=True))
stopSRC = 0
stopDST = 0
for key, value in sortSrc.items():          #output sorted src Ips
    stopSRC += 1
    if key[:-3] == ‘exclude’ or key[:-4] == ‘exclude’: pass
    else: print('src', value, key)          #if stmnt is for the IP exclusion
    if stopSCR > 30:
    break
print()
for key, value in sortDst.items():          #output sorted dst Ips
    stopDST += 1
    if key[:-3] == ‘exclude’ or key[:-4] == ‘exclude’: pass
    else: print(‘dst’, value, key)          #if stmnt is for the IP exclusion
    if stopDST > 30:
    break
