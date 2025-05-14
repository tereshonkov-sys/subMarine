file = open("лорх.txt", "r", encoding='utf-8')
loreh=file.read().splitlines()
file.close()
file = open("лор1.txt", "r", encoding='utf-8')
lore1=file.read().splitlines()
file.close()
file = open("hs.txt", "r", encoding='utf-8')
his=file.read().splitlines()
file.close()
file = open("end1.txt", "r", encoding='utf-8')
bed=file.read().splitlines()
file.close()
file = open("end2.txt", "r", encoding='utf-8')
good=file.read().splitlines()
file.close()
drop = [[42.21,'секретное'],[0.3,'БРОНЕПРОБИВАТЕЛИ'],[0.5, "Торпеда Mk-1"],[0.3, "Электромагнитный импульс (ЭМИ)"],[0.9, "Кластерная торпеда"],
        [1.2, "Тяжелая бронебойная торпеда"],[0.4, "Сонарный маячок"],[0.6, "Кислотный заряд"],[1.5, "Ядерная торпеда 'Посейдон'"],[0.2,'зажигательные']]
location = [[2,[0,0,1.0,0.1],],#y,x,хп.скорость
            [2,[0,0,10.0,0.1],drop[1]],
            [2,[0,0,5.0,0.2],drop[2]],
            [2,[0,0,50.0,0.05],drop[3]],
            [2,[0,0,5.5,0.3],drop[4]],
            [2,[0,0,25.0,0.1],drop[5]],
            [2,[0,0,100.0,0.04],drop[6]],
            [2,[0,0,50.0,0.07],drop[7]],
            [2,[0,0,8.0,0.4],drop[8]],
            [2,[0,0,500.0,0.05],drop[9]]
            ]
subst = [['призрак',1.5,1.5,1.5,2],
         ['корыто',10,5,1,1000],
         ['просто подлодка',1,1,1,1],
         ['адмирал',0.5,3.5,0.5,0.5]]