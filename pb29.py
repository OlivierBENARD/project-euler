def pb29(lim):
  print(len(set((i**j for j in range(2, lim+1) for i in range(2, lim+1)))))

pb29(100)
