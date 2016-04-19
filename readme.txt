wald = agentsEvoltuion.getWealthArray(waldRS, priceX)
plt.plot(np.linspace(0, len(wald), len(wald)), wald)

#wald = agentsEvoltuion.getWealthArray(waldRS, priceX)
#plt.plot(np.linspace(0, len(wald), len(wald)), wald)
#plt.draw()

nb, NB = 0.001, []
for i in range(10):
    rate = 0.25
    nb *= (1 + rate)
    NB.append(nb)

