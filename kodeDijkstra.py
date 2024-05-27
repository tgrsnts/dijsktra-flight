class graph:
    def __init__(self,n):
        self.takhingga = 9999999999
        self.V = []
        self.adjcMatrix = []
        #daftar verteks pada graph
        for i in range(n):
            v = vertex(i)
            self.V.append(v)
        #buat adjacency matrix
        for i in range(n):
            row = []
            for j in range(n):
                row.append(0)
            self.adjcMatrix.append(row)

    def printVertex(self):
        nV = len(self.V)
        print("id\twarna\tid pred.\tdistance")
        print("---------------------------------------------")
        for i in range(nV):
            #untuk warna
            if self.V[i].color == None:
                warna = "N/A"
            elif self.V[i].color == 0:
                warna = "putih"
            elif self.V[i].color == 1:
                warna = "abu-abu"

            #untuk pred
            if self.V[i].pred == None:
                prednya = "N/A"
            else:
                prednya = "v"+ str(self.V[i].pred)

            #untuk distance
            if self.V[i].distance == None or self.V[i].distance == self.takhingga:
                print("%d\t%s\t  %s\t         inf"%(i,warna,prednya))    
            else:
                print("%d\t%s\t  %s\t         %d"%(i,warna,prednya,self.V[i].distance))  

    def printAdjcMatrix(self):
        ukuran = len(self.adjcMatrix)
        print("\nAdjacency Matriks:")
        print("    ",end="")
        for i in range(ukuran):
            print(" [%d]"%(i), end="  ")
        print("")
        for i in range(ukuran):
            print("[%d]"%(i), end="  ")
            for j in range(ukuran):
                print("%2d"%(self.adjcMatrix[i][j]),end="    ")
            print("")
    
    def addEdge(self,u,v,w):
        self.adjcMatrix[u][v] = w

    def dijkstraShortestPath(self,v_awal,v_tujuan):
        print("\nALGORITMA DIJKSTRA DIJALANKAN")
        print("---------------------------------------------")
        print("Mencari Shortest Path dari v%d ke v%d"%(v_awal,v_tujuan))
        #inisialisasi
        bnykV = len(self.V)
        for i in range(bnykV):
            self.V[i].color = 0
            self.V[i].distance = self.takhingga
        self.V[v_awal].distance = 0

        print("\n>> Setelah tahapan inisialisasi")
        G.printVertex()    
        #memilih u
        u = None
        it = 1
        while u != v_tujuan:
            print("\nIterasi ke",it," >>> ") 
            it +=1
            u = None
            for i in range(bnykV):
                if u==None and self.V[i].color == 0 and self.V[i].distance != self.takhingga:
                    u = i
                elif self.V[i].color == 0  and self.V[i].distance < self.V[u].distance:
                    u = i
            print("Terpilih vertex",u)
            self.V[u].color = 1
                
            #mengeksplorasi graph dengan acuan vertex u
            for i in range(bnykV):
                #syarat dicek vi masih putih dan ada edge dari u ke vi
                if self.V[i].color == 0 and self.adjcMatrix[u][i] != 0:
                    # syarat update terjadi jika, dist rute baru lebih pendek < dist rute lama
                    # distance rute baru = self.V[u].distance + self.adjcMatrix[u][i]
                    # distance rute lama disimpan pada  =  self.V[i].distance 
                    if self.V[u].distance + self.adjcMatrix[u][i] < self.V[i].distance:
                        self.V[i].distance = self.V[u].distance + self.adjcMatrix[u][i]
                        print("distance ke v%d terupdate jadi %d"%(i,self.V[i].distance))
                        self.V[i].pred = u
            G.printVertex()

        print("Pathnya:", end=" ")
        self.ektrakPath(v_awal,v_tujuan)
        print("dengan distance:", self.V[v_tujuan].distance)
        

    def ektrakPath(self,awal,akhir):
        #print(awal,akhir)
        if awal != akhir:
            self.ektrakPath(awal,self.V[akhir].pred)
            print("v"+str(akhir),end=" ")
        else:
            print("v"+str(akhir),end=" ")

            





    
    
class vertex:
    def __init__(self,id):
        self.id = id
        self.color = None #0 putih S, 1 abu S'
        self.pred = None
        self.distance = None
    
#---------------------------------------------
#PROGRAM UTAMA
f = open("data_graph01_directed.txt","r")
nV,nE = f.readline().split(" ")
nV = int(nV)
nE = int(nE)
print("Program shortest Path dengan Dijkstra")
print("---------------------------------------------------------------------")
print("Jumlah Verteks:",nV)
print("Jumlah Edge:",nE)

G = graph(nV)
#G.printVertex()
#G.printVertex()
#print(G.adjcMatrix)
G.printAdjcMatrix()
#membaca edge dari file---------------------------
print("\nTahapan Program membaca data edge:")
print("---------------------------------------------------------------------")
for i in range(nE):
    u,v,bobot = f.readline().split(" ")
    u = int(u)
    v = int(v)
    bobot = int(bobot)
    print("Edge ke-%d dari v%d ke v%d dengan bobot %d"%(i+1,u,v,bobot))
    G.addEdge(u,v,bobot)

    

G.printAdjcMatrix()

G.dijkstraShortestPath(0,5)
#G.printVertex()