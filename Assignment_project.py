def my_function(day):
    import random
    LIST=['chicken','beef','fish','veggie','Rice','lady-finger','mix_vegetable','daal mash','daal mong','briyani','chese','mashroom','mutton']
    list_chicken=['chicken','chicken karahi','chicken white karahi','chicken ginger','chicken ginger karahi','chicken white karahi','chicken white gin']
    list_beef=['beef','beef karahi','beef white karahi','beef ginger','beef ginger karahi','beef white karahi','beef white gin']
    list_fish=['fish','fish karahi','fish white karahi','fish ginger','fish ginger karahi','fish white karahi','fish white gin']
    list_veggie=['veggie','veggie karahi','veggie white karahi','veggie ginger','veggie ginger karahi','veggie white karahi','veggie white gin']
    list_Rice=['Rice','Rice karahi','Rice white karahi','Rice ginger','Rice ginger karahi','Rice white karahi','Rice white gin']
    list_lady_finger=['lady-finger','lady-finger karahi','lady-finger white karahi','lady-finger ginger','lady-finger ginger karahi','lady-finger white karahi','lady-finger white gin']
    list_mix_vegetable=['mix_vegetable','mix_vegetable karahi','mix_vegetable white karahi','mix_vegetable ginger','mix_vegetable ginger karahi','mix_vegetable white karahi','mix_vegetable white gin']
    list_daal_mash=['daal mash','daal mash karahi','daal mash white karahi','daal mash ginger','daal mash ginger karahi','daal mash white karahi','daal mash white gin']
    list_daal_mong=['daal mong','daal mong karahi','daal mong white karahi','daal mong ginger','daal mong ginger karahi','daal mong white karahi','daal mong white gin']
    list_briyani=['briyani','briyani karahi','briyani white karahi','briyani ginger','briyani ginger karahi','briyani white karahi','briyani white gin']
    list_chese=['chese','chese karahi','chese white karahi','chese ginger','chese ginger karahi','chese white karahi','chese white gin']
    list_mashroom=['mashroom','mashroom karahi','mashroom white karahi','mashroom ginger','mashroom ginger karahi','mashroom white karahi','mashroom white gin']
    list_mutton=['mutton','mutton karahi','mutton white karahi','mutton ginger','mutton ginger karahi','mutton white karahi','mutton white gin']
    list_order=[]
    if day==1:
        print('Today"s is Monday so we have these dishes available')
    elif day==2:
        print('Today"s is Tuesday so we have these dishes available')
    elif day==3:
        print('Today"s is Wednesday so we have these dishes available')
    elif day==4:
        print('Today"s is Thursday so we have these dishes available')
    elif day==5:
        print('Today"s is Friday so we have these dishes available')
    elif day==6:
        print('Today"s is Saturday so we have these dishes available')
    elif day==7:
        print('Today"s is Sunday so we have these dishes available')
    for i in range(6):
        x=random.choice(LIST)
        print('Todays our',i+1,' dish is :',x)
        list_order.append(x)
    print('Your order is :',list_order)
    print('select your dishes from Toyday"s menu')
    print('1 for first dish,2 for second dish,3 for third dish,4 for fourth dish,5 for fifth dish,6 for sixth dish')
    dish_no=int(input('Enter the dish number: '))
    total_dish=int(input('Total number of dish that you want to eat: '))
    for i in range(total_dish+1):
        if dish_no==1:
            x=list_order[0]
            print('so If you want to eat', x ,  ' then we have these dishes available in this category')
            for i in range(3):
                if x in list_chicken:
                    print('Todays our',i+1,' dish is :',random.choice(list_chicken))
                elif x in list_beef:
                    print('Todays our',i+1,' dish is :',random.choice(list_beef))
                elif x in list_fish:
                    print('Todays our',i+1,' dish is :',random.choice(list_fish))
                elif x in list_veggie:
                    print('Todays our',i+1,' dish is :',random.choice(list_veggie))
                elif x in list_Rice:
                    print('Todays our',i+1,' dish is :',random.choice(list_Rice))
                elif x in list_lady_finger:
                    print('Todays our',i+1,' dish is :',random.choice(list_lady_finger))
                elif x in list_mix_vegetable:
                    print('Todays our',i+1,' dish is :',random.choice(list_mix_vegetable))
                elif x in list_daal_mash:
                    print('Todays our',i+1,' dish is :',random.choice(list_daal_mash))
                elif x in list_daal_mong:
                    print('Todays our',i+1,' dish is :',random.choice(list_daal_mong))
                elif x in list_briyani:
                    print('Todays our',i+1,' dish is :',random.choice(list_briyani))
                elif x in list_chese:
                    print('Todays our',i+1,' dish is :',random.choice(list_chese))
                elif x in list_mashroom:
                    print('Todays our',i+1,' dish is :',random.choice(list_mashroom))
                elif x in list_mutton:
                    print('Todays our',i+1,' dish is :',random.choice(list_mutton))
                else:
                    pass
            
                print('Todays our',i+1,' dish is :',random.choice(list_chick))
        elif dish_no==2:
            x=list_order[1]
            print('so If you want to eat', x ,  ' then we have these dishes available in this category')
            for i in range(3):
                if x in list_chicken:
                    print('Todays our',i+1,' dish is :',random.choice(list_chicken))
                elif x in list_beef:
                    print('Todays our',i+1,' dish is :',random.choice(list_beef))
                elif x in list_fish:
                    print('Todays our',i+1,' dish is :',random.choice(list_fish))
                elif x in list_veggie:
                    print('Todays our',i+1,' dish is :',random.choice(list_veggie))
                elif x in list_Rice:
                    print('Todays our',i+1,' dish is :',random.choice(list_Rice))
                elif x in list_lady_finger:
                    print('Todays our',i+1,' dish is :',random.choice(list_lady_finger))
                elif x in list_mix_vegetable:
                    print('Todays our',i+1,' dish is :',random.choice(list_mix_vegetable))
                elif x in list_daal_mash:
                    print('Todays our',i+1,' dish is :',random.choice(list_daal_mash))
                elif x in list_daal_mong:
                    print('Todays our',i+1,' dish is :',random.choice(list_daal_mong))
                elif x in list_briyani:
                    print('Todays our',i+1,' dish is :',random.choice(list_briyani))
                elif x in list_chese:
                    print('Todays our',i+1,' dish is :',random.choice(list_chese))
                elif x in list_mashroom:
                    print('Todays our',i+1,' dish is :',random.choice(list_mashroom))
                elif x in list_mutton:
                    print('Todays our',i+1,' dish is :',random.choice(list_mutton))
                else:
                    pass
        elif dish_no==3:
            x=list_order[2]
            print('so If you want to eat', x ,  ' then we have these dishes available in this category')
            for i in range(3):
                if x in list_chicken:
                    print('Todays our',i+1,' dish is :',random.choice(list_chicken))
                elif x in list_beef:
                    print('Todays our',i+1,' dish is :',random.choice(list_beef))
                elif x in list_fish:
                    print('Todays our',i+1,' dish is :',random.choice(list_fish))
                elif x in list_veggie:
                    print('Todays our',i+1,' dish is :',random.choice(list_veggie))
                elif x in list_Rice:
                    print('Todays our',i+1,' dish is :',random.choice(list_Rice))
                elif x in list_lady_finger:
                    print('Todays our',i+1,' dish is :',random.choice(list_lady_finger))
                elif x in list_mix_vegetable:
                    print('Todays our',i+1,' dish is :',random.choice(list_mix_vegetable))
                elif x in list_daal_mash:
                    print('Todays our',i+1,' dish is :',random.choice(list_daal_mash))
                elif x in list_daal_mong:
                    print('Todays our',i+1,' dish is :',random.choice(list_daal_mong))
                elif x in list_briyani:
                    print('Todays our',i+1,' dish is :',random.choice(list_briyani))
                elif x in list_chese:
                    print('Todays our',i+1,' dish is :',random.choice(list_chese))
                elif x in list_mashroom:
                    print('Todays our',i+1,' dish is :',random.choice(list_mashroom))
                elif x in list_mutton:
                    print('Todays our',i+1,' dish is :',random.choice(list_mutton))
                else:
                    pass
        elif dish_no==4:
            x=list_order[3]
            print('so If you want to eat', x ,  ' then we have these dishes available in this category')
            for i in range(3):
                if x in list_chicken:
                    print('Todays our',i+1,' dish is :',random.choice(list_chicken))
                elif x in list_beef:
                    print('Todays our',i+1,' dish is :',random.choice(list_beef))
                elif x in list_fish:
                    print('Todays our',i+1,' dish is :',random.choice(list_fish))
                elif x in list_veggie:
                    print('Todays our',i+1,' dish is :',random.choice(list_veggie))
                elif x in list_Rice:
                    print('Todays our',i+1,' dish is :',random.choice(list_Rice))
                elif x in list_lady_finger:
                    print('Todays our',i+1,' dish is :',random.choice(list_lady_finger))
                elif x in list_mix_vegetable:
                    print('Todays our',i+1,' dish is :',random.choice(list_mix_vegetable))
                elif x in list_daal_mash:
                    print('Todays our',i+1,' dish is :',random.choice(list_daal_mash))
                elif x in list_daal_mong:
                    print('Todays our',i+1,' dish is :',random.choice(list_daal_mong))
                elif x in list_briyani:
                    print('Todays our',i+1,' dish is :',random.choice(list_briyani))
                elif x in list_chese:
                    print('Todays our',i+1,' dish is :',random.choice(list_chese))
                elif x in list_mashroom:
                    print('Todays our',i+1,' dish is :',random.choice(list_mashroom))
                elif x in list_mutton:
                    print('Todays our',i+1,' dish is :',random.choice(list_mutton))
                else:
                    pass    
        elif dish_no==5:
            x=list_order[4]
            print('so If you want to eat', x ,  ' then we have these dishes available in this category')
            for i in range(3):
                if x in list_chicken:
                    print('Todays our',i+1,' dish is :',random.choice(list_chicken))
                elif x in list_beef:
                    print('Todays our',i+1,' dish is :',random.choice(list_beef))
                elif x in list_fish:
                    print('Todays our',i+1,' dish is :',random.choice(list_fish))
                elif x in list_veggie:
                    print('Todays our',i+1,' dish is :',random.choice(list_veggie))
                elif x in list_Rice:
                    print('Todays our',i+1,' dish is :',random.choice(list_Rice))
                elif x in list_lady_finger:
                    print('Todays our',i+1,' dish is :',random.choice(list_lady_finger))
                elif x in list_mix_vegetable:
                    print('Todays our',i+1,' dish is :',random.choice(list_mix_vegetable))
                elif x in list_daal_mash:
                    print('Todays our',i+1,' dish is :',random.choice(list_daal_mash))
                elif x in list_daal_mong:
                    print('Todays our',i+1,' dish is :',random.choice(list_daal_mong))
                elif x in list_briyani:
                    print('Todays our',i+1,' dish is :',random.choice(list_briyani))
                elif x in list_chese:
                    print('Todays our',i+1,' dish is :',random.choice(list_chese))
                elif x in list_mashroom:
                    print('Todays our',i+1,' dish is :',random.choice(list_mashroom))
                elif x in list_mutton:
                    print('Todays our',i+1,' dish is :',random.choice(list_mutton))
                else:
                    pass
        elif dish_no==6:
            x=list_order[5]
            print('so If you want to eat', x ,  ' then we have these dishes available in this category')
            for i in range(3):
                if x in list_chicken:
                    print('Todays our',i+1,' dish is :',random.choice(list_chicken))
                elif x in list_beef:
                    print('Todays our',i+1,' dish is :',random.choice(list_beef))
                elif x in list_fish:
                    print('Todays our',i+1,' dish is :',random.choice(list_fish))
                elif x in list_veggie:
                    print('Todays our',i+1,' dish is :',random.choice(list_veggie))
                elif x in list_Rice:
                    print('Todays our',i+1,' dish is :',random.choice(list_Rice))
                elif x in list_lady_finger:
                    print('Todays our',i+1,' dish is :',random.choice(list_lady_finger))
                elif x in list_mix_vegetable:
                    print('Todays our',i+1,' dish is :',random.choice(list_mix_vegetable))
                elif x in list_daal_mash:
                    print('Todays our',i+1,' dish is :',random.choice(list_daal_mash))
                elif x in list_daal_mong:
                    print('Todays our',i+1,' dish is :',random.choice(list_daal_mong))
                elif x in list_briyani:
                    print('Todays our',i+1,' dish is :',random.choice(list_briyani))
                elif x in list_chese:
                    print('Todays our',i+1,' dish is :',random.choice(list_chese))
                elif x in list_mashroom:
                    print('Todays our',i+1,' dish is :',random.choice(list_mashroom))
                elif x in list_mutton:
                    print('Todays our',i+1,' dish is :',random.choice(list_mutton))
                else:
                    pass
        else:
            pass
import random        
print('1 for Monday,2 for Tuesday,3 for Wednesday,4 for Thursday,5 for Friday,6 for Saturday,7 for Sunday')

day=int(input('Enter the day: '))
if day>7 or day<1:
    while day>7 or day<1:
        print('invalid input')
        print('1 for Monday,2 for Tuesday,3 for Wednesday,4 for Thursday,5 for Friday,6 for Saturday,7 for Sunday')
        day=int(input('Again Enter the day: '))
my_function(day)
sweet=input('Are you want to like any sweet dish?(yes(press y/Y)/no(press n/N) ')
if sweet=='Y' or sweet=='y':
   List_sweet=['kheer','custard','icecream','jelly','gajar ka halwa','gulab jamun','ras malai','ras gulla','jalebi','gajar ka halwa','gulab jamun','ras malai','ras gulla','jalebi']
   sweet_select=[]
   for i in range(3):
       x=random.choice(List_sweet)
       print('Todays our',i+1,' sweet dish is :',x)
       sweet_select.append(x)
   print('which one that you want to eat?')
   print('1 for first sweet dish,2 for second sweet dish,3 for third sweet dish')
   sweet_no=int(input('Enter the sweet dish number: '))
   if sweet_no==1:
       x=sweet_select[sweet_no-1]
       print('so you want to eat',x)
       print('its too much delicious, you must try it')
   elif sweet_no==2:
        x=sweet_select[sweet_no-1]
        print('so you want to eat',x)
        print('its too much delicious, you must try it')
   elif sweet_no==3:
        x=sweet_select[sweet_no-1]
        print('so you want to eat',x)
        print('its too much delicious, you must try it')
elif sweet=='N' or sweet=='n':
    print('ok as you wish sir, but we have these sweet dishes available')
else:
    print('invalid input')

print('Thank you for using our service')