def help_from_sam(a):
    count=1
    n=1
    while n*2<=a:
        n*=2
    return count+(a-n)

a=int(input())
print(help_from_sam(a))