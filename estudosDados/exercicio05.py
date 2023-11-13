
# 4 - Utilizar o modelo de regressão logistica treinado para fazer classificação  
  
  
previsto=pipe.predict(x_teste[0].reshape(1,-1))
real = y_teste[0]
print('previsto:{}; real{}'.format(previsto[0],real))
