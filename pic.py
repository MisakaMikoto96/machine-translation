import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4, 5, 6]
y1 = [8.518987145,10.5363676,11.9584482,12.8703166,14.30517329,14.39836517]

x2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y2 = [10.0833585,10.80214943,11.44679975,11.78526849,12.5014241,12.67700757,13.60861406,14.04126506,14.15132751,14.8292569,14.84390334,15.00024433]

x3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12]
y3 = [8.369034473,11.41181021,12.70459448,13.8590909,14.2788356,15.1132584,15.53546406,15.73511402,16.64641233,16.93561307,18.47079754,18.16756056]

x4 = [1, 2, 3, 4, 5, 6]
y4 = [8.268091381,10.07899368,11.10714998,12.53233457,13.13374358,14.05808254]

x5 = [1, 2, 3, 4, 5, 6]
y5 = [9.5703891,10.81367212,10.65756656,11.02668588,11.96484148,13.01274169]

x6 = [1, 2, 3, 4, 5, 6]
y6 = [7.812841005,7.748799773,8.595496901,9.825115628,10.44672381,10.51167216]

x7 = [1, 2, 3, 4, 5, 6]
y7 = [6.929391514,8.655220095,9.975679686,11.65792646,12.42937478,13.16210522]

x8 = [1, 2, 3, 4, 5, 6]
y8 = [7.284230836,9.300866858,10.00598268,11.21742669,11.08108075,11.89884141]

group_labels = ['1','2','3','4','5','6','7','8','9','10','11','12']
plt.title('The change of BLEU')
plt.xlabel('epoch')
plt.ylabel('BLEU')

plt.plot(x1, y1,'r', label='1-1-12-NAND')
plt.plot(x2, y2,'b',label='1-1-24-NAD')
plt.plot(x3, y3,'g',label='1-1-24-AND')
plt.plot(x4, y4,'yellow',label='1-1-12-AD')
plt.plot(x5, y5,'pink',label='2-3-12-NAND')
plt.plot(x6, y6,'olive',label='2-3-12-NAD')
plt.plot(x7, y7,'navy',label='2-3-12-AND')
plt.plot(x8, y8,'black',label='2-3-12-AD')

plt.xticks(x1, group_labels, rotation=0)
'''
plt.plot(x3, y3, 'r', label='broadcast')
plt.plot(x4, y4, 'b', label='join')
plt.xticks(x3, group_labels, rotation=0)
'''
plt.legend(bbox_to_anchor=[0.3, 1])
plt.grid()
plt.show()  