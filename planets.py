def weight_on_planets():
    weight = int(input('What do you weigh on earth? '))
    print('\nOn Mars you would weigh ' + str(weight * 0.38) + ' pounds.\n'
        + 'On Jupiter you would weigh ' + str(weight * 2.34) + ' pounds.')
   
   
if __name__ == '__main__':
   weight_on_planets()