from tkinter import *
from tkinter import messagebox

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
    # Membuat GUI menggunakan tkinter
    root = Tk()
    root.title("Aplikasi Rute Penerbangan")
    root.geometry("600x400")
    font_style = ("Calibri", 9)

    def find_shortest_path():
        asal = entry_bandara_asal.get().strip()
        tujuan = entry_bandara_tujuan.get().strip()
        
        if asal not in vertex_map or tujuan not in vertex_map:
            messagebox.showerror("Error", "Bandara tidak ditemukan.")
            return
        
        v_awal = vertex_map[asal]
        v_tujuan = vertex_map[tujuan]
        
        path, total_distance = G.dijkstra_shortest_path(v_awal, v_tujuan)
        if not path:
            result_text.set("Tidak ada jalur dari bandara asal ke tujuan.")
            return
        
        result = "Jalur yang dilalui:\n"
        for i in range(len(path)):
            for bandara, idx in vertex_map.items():
                if idx == path[i]:
                    if i == len(path) - 1:
                        result += f"{bandara} "
                    else:
                        result += f"{bandara} -> "
        result += f"\nTotal jarak: {total_distance}"
        result_text.set(result)

    label_bandara_asal = Label(root, text="Bandara Asal:", fg="black", font=font_style)
    label_bandara_asal.grid(row=0, column=0, sticky=W, padx=10, pady=10)
    entry_bandara_asal = Entry(root, font=font_style)
    entry_bandara_asal.grid(row=0, column=1, padx=10, pady=10)

    label_bandara_tujuan = Label(root, text="Bandara Tujuan:", fg="black", font=font_style)
    label_bandara_tujuan.grid(row=1, column=0, sticky=W, padx=10, pady=10)
    entry_bandara_tujuan = Entry(root, font=font_style)
    entry_bandara_tujuan.grid(row=1, column=1, padx=10, pady=10)

    button_cari = Button(root, text="Cari Jalur Tercepat", command=find_shortest_path, font=font_style)
    button_cari.grid(row=2, column=0, columnspan=2, pady=20)

    result_text = StringVar()
    label_hasil = Label(root, textvariable=result_text, fg="black", font=font_style, justify=LEFT)
    label_hasil.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    label_daftar_bandara = Label(root, text="Daftar Bandara:", fg="black", font=font_style)
    label_daftar_bandara.grid(row=0, column=2, sticky=W, padx=10, pady=10)
    listbox_bandara = Listbox(root, font=font_style)
    listbox_bandara.grid(row=1, column=2, rowspan=3, padx=10, pady=10)

    filename = 'data_graph.txt'
    nV, edges, vertex_map = read_graph_from_file(filename)

    G = Graph(nV)
    for u, v, w in edges:
        G.add_edge(vertex_map[u], vertex_map[v], w)

    for bandara in vertex_map:
        listbox_bandara.insert(END, bandara)

    root.mainloop()

if __name__ == "__main__":
    main()
