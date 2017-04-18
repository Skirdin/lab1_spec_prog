import urllib.request
import urllib.parse
import pandas as pd


def download(provinceID):

    params = urllib.parse.urlencode({'country': 'UKR', 'provinceID': provinceID, 'year1': 1981, 'year2': 2017, 'type': 'Mean'})
    url = "https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?%s" % params
    vhi_url = urllib.request.urlopen(url)
    csvn = 'vhi_id_' + provinceID + '.csv'
    out = open(csvn, 'wb')
    out.write(vhi_url.read())
    out.close()
    f = open(csvn, 'r')
    s = f.read()
    s = s.replace(s[0:s.find('\n')],'year,week,SMN,SMT,VCI,TCI,VHI')
    s = s.replace("</pre></tt>", '')
    ns = ''
    j = 0
    while j+3 < len(s):
        ns += s[j]
        if s[j].isdigit() and ((s[j+1] == ' ' and s[j+2].isdigit() and not(s[j+3] == '\n')) or (s[j+1] == ' ' and s[j+2] == ' 'and s[j+3].isdigit())):
            ns += ','
        j += 1
    ns += s[j]
    ns += s[j+1]
    ns += s[j+2]
    s = ns
    s = s.replace(' ', '')
    f.close()
    fo = open(csvn, 'w')
    fo.write(s)
    fo.close()


def clr(s) :
    i = 2
    c = 0
    while i+2 < len(s):
        if s[i] == '\n':
            c = 0
        if s[i] == ',':
            c +=1
        if c != 6 and s[i+1]=='\n':
            s = s.replace(s[s.rfind('\n', 0, i):s.rfind('\n', i, len(s) - 1)+1], '')
        if (s[i] == ',' and (not s[i-1].isdigit() )  and not( s[i+1].isdigit() or s[i+1] == '\n')):
            s = s.replace(s[s.rfind('\n', 0, i):s.rfind('\n', i, len(s) - 1) + 1], '')
        i += 1
    return s
# i=1
# while i<28 :
#     download(str(i))
#     i+=1

# df = pd.read_csv('vhi_id_3.csv')
# # print (df.loc[df['year'] == 2016, 'VHI'])
# # print ('max: ',df.loc[df['year'] == 2016, 'VHI'].max())
# # print ('min: ',df.loc[df['year'] == 2016, 'VHI'].min())
#
# print(df.loc[df['VHI']<35, 'VHI'])

f = open('vhi_id_1_1.csv', 'r')
s=f.read()
i = 1
c = 0
while i+1 < len(s):
    if s[i] == '\n':
        c = 0
    if s[i] == ',':
        c += 1
    if s[i]==',' and s[i+1]==',' :
        s = s.replace(s[s.rfind('\n', 0, i)+1:s.find('\n', i, len(s) - 1) + 1], '')
    i += 1
s=s.replace("\n\n","\n")
print(s)