def quadrant(x, y):
    #Carlos ALberto Mendoza Medina A01661896
    
    if x==0 and y==0:
        return('Origin')
    elif x==0 and y!=0:
        return('eje Y')
    elif y==0 and x!=0:
        return('eje X')
    elif x>0 and y>0:
        return('I')
    elif x<0 and y>0:
        return('II')
    elif x<0 and y<0:
        return('III')
    elif x>0 and y<0:
        return('IV')
        
def main():
    x = float(input("Enter X coordinate of the point: "))
    y = float(input("Enter Y coordinate of the point: "))
    print(f"The point is in quadrant: {quadrant(x, y)}")


if __name__ == '__main__':
    main()
