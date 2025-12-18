a = [
    "192.168.1.1 - GET /index.html 200",
    "192.168.1.5 - GET /about 404",
    "192.168.1.1 - POST /login 200",
    "10.0.0.1 - GET /admin 500",
    "192.168.1.1 - GET /home 404",
    "192.168.1.5 - GET /contact 404",
    "10.0.0.1 - POST /api 500",
    "192.168.1.1 - GET /page 500",
    "192.168.1.1 - GET /test 404",
    "192.168.1.5 - GET /user 404"
]
b = {"200": 0, "404": 0, "500": 0}
c = {}
d = {}
n = 2
for i in a:
    p = i.split()
    if len(p) >= 4:
        ip = p[0]
        cd = p[-1]
        
        if cd in b:
            b[cd] += 1
        
        c[ip] = c.get(ip, 0) + 1
        
        if cd in ["404", "500"]:
            d[ip] = d.get(ip, 0) + 1
m = max(c, key=c.get)
s = [ip for ip, cnt in d.items() if cnt > n]
print("1. Коды ответов:")
for cd, cnt in b.items():
    print(f"   Код {cd}: {cnt}")
print(f"\n2. IP с наибольшим количеством запросов: {m} ({c[m]} запросов)")
print(f"\n3. Подозрительные IP (>{n} ошибок 404/500):")
if s:
    for ip in s:
        print(f"   {ip}: {d[ip]} ошибок")
else:
    print("   Нет подозрительных IP")
