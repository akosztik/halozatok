def szokoev(ev):
    if ev%4==0:
        if ev%100==0:
            if ev%400==0:
                return True
            return False
        return True
    return False

print szokoev(2000)
print szokoev(1993)


