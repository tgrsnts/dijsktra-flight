class Graph:
    def __init__(self, n):
        self.takhingga = 9999999999
        self.V = []
        self.adjcMatrix = []
        for i in range(n):
            v = Vertex(i)
            self.V.append(v)
        for i in range(n):
            row = [0] * n
            self.adjcMatrix.append(row)

    def add_edge(self, u, v, w):
        self.adjcMatrix[u][v] = w

    def dijkstra_shortest_path(self, v_awal, v_tujuan):
        bnykV = len(self.V)
        for i in range(bnykV):
            self.V[i].color = 0
            self.V[i].distance = self.takhingga
            self.V[i].pred = None
        self.V[v_awal].distance = 0

        while True:
            u = None
            for i in range(bnykV):
                if self.V[i].color == 0 and (u is None or self.V[i].distance < self.V[u].distance):
                    u = i
            if u is None or self.V[u].distance == self.takhingga:
                break

            self.V[u].color = 1

            for i in range(bnykV):
                if self.V[i].color == 0 and self.adjcMatrix[u][i] != 0:
                    if self.V[u].distance + self.adjcMatrix[u][i] < self.V[i].distance:
                        self.V[i].distance = self.V[u].distance + self.adjcMatrix[u][i]
                        self.V[i].pred = u

        path, total_distance = self.extract_path(v_awal, v_tujuan)
        return path, total_distance

    def extract_path(self, awal, akhir):
        path = []
        total_distance = self.V[akhir].distance
        while akhir is not None:
            path.insert(0, akhir)
            akhir = self.V[akhir].pred
        if self.V[path[0]].distance == self.takhingga:
            return [], None
        return path, total_distance

class Vertex:
    def __init__(self, id):
        self.id = id
        self.color = None
        self.pred = None
        self.distance = None

def read_graph_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        nV, nE = map(int, lines[0].split())
        edges = []
        vertex_map = {}
        index = 0
        for line in lines[1:]:
            u, v, w = line.split()
            if u not in vertex_map:
                vertex_map[u] = index
                index += 1
            if v not in vertex_map:
                vertex_map[v] = index
                index += 1
            edges.append((u, v, int(w)))
        return nV, edges, vertex_map

def main():
    filename = 'data_graph.txt'
    nV, edges, vertex_map = read_graph_from_file(filename)

    G = Graph(nV)
    for u, v, w in edges:
        G.add_edge(vertex_map[u], vertex_map[v], w)

    print("Daftar Bandara:")
    for bandara in vertex_map:
        print(bandara)

    asal = input("Masukkan bandara asal: ").strip()
    tujuan = input("Masukkan bandara tujuan: ").strip()

    if asal not in vertex_map or tujuan not in vertex_map:
        print("Bandara tidak ditemukan.")
        return

    v_awal = vertex_map[asal]
    v_tujuan = vertex_map[tujuan]

    path, total_distance = G.dijkstra_shortest_path(v_awal, v_tujuan)
    if not path:
        print("Tidak ada jalur dari bandara asal ke tujuan.")
        return

    print("Jalur yang dilalui:")
    for i in range(len(path)):
        for bandara, idx in vertex_map.items():
            if idx == path[i]:
                if i == len(path) - 1:
                    print(bandara, end=" ")
                else:
                    print(bandara, end=" -> ")
    print(f"\nTotal jarak: {total_distance}")

if __name__ == "__main__":
    main()