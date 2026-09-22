import numpy as np
np.set_printoptions(precision=2, suppress=True)
toks = ["the","cat","sat","on"]
# embeddings de juguete, 4 tokens x d=4, enteros chicos
X = np.array([[1,0,1,0],
              [0,2,0,1],
              [1,1,1,1],
              [0,1,1,2]], float)
Wq = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], float)   # identidad: Q = X
Wk = np.array([[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]], float)   # permuta pares de columnas
Wv = np.array([[1,0],[0,1],[1,0],[0,1]], float)                    # 4 -> 2, suma pares
Q, K, V = X@Wq, X@Wk, X@Wv
S = Q@K.T
Ssc = S/np.sqrt(4)
def softmax(a): e=np.exp(a-a.max(-1,keepdims=True)); return e/e.sum(-1,keepdims=True)
A = softmax(Ssc)
O = A@V
mask = np.triu(np.ones((4,4)),1).astype(bool)
Am = softmax(np.where(mask,-np.inf,Ssc))
Om = Am@V
for n,m in [("X",X),("Q=XWq",Q),("K=XWk",K),("V=XWv",V),("QK^T",S),("QK^T/sqrt(d)",Ssc),("softmax (filas)",A),("salida A V",O),("mascara causal: softmax",Am),("salida causal",Om)]:
    print(f"--- {n}\n{m}")
