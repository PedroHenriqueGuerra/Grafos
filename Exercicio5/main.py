from grafo import Grafo

grafo = Grafo()

grafo.adicionaVertice("v1")
grafo.adicionaVertice("v2")
grafo.adicionaVertice("v3")
grafo.adicionaVertice("v4")
grafo.adicionaVertice("v5")
grafo.adicionaVertice("v6")
grafo.adicionaVertice("v7")
grafo.adicionaVertice("v8")
grafo.adicionaVertice("v9")
grafo.adicionaVertice("v10")
grafo.adicionaVertice("v11")
grafo.adicionaVertice("v12")
grafo.adicionaVertice("v13")
grafo.adicionaVertice("v14")
grafo.adicionaVertice("v15")
grafo.adicionaVertice("v16")
grafo.adicionaVertice("v17")
grafo.adicionaVertice("v18")
grafo.adicionaVertice("v19")
grafo.adicionaVertice("v20")
grafo.adicionaVertice("v21")
grafo.adicionaVertice("v22")
grafo.adicionaVertice("v23")
grafo.adicionaVertice("v24")
grafo.adicionaVertice("v25")
grafo.adicionaVertice("v26")
grafo.adicionaVertice("v27")
grafo.adicionaVertice("v28")
grafo.adicionaVertice("v29")
grafo.adicionaVertice("v30")
grafo.adicionaVertice("v31")
grafo.adicionaVertice("v32")
grafo.adicionaVertice("v33")


# V1
grafo.adicionaAresta("a1", "v1-v2")
grafo.adicionaAresta("a2", "v1-v3")
grafo.adicionaAresta("a3", "v1-v4")

#V2
grafo.adicionaAresta("a4", "v2-v3")
grafo.adicionaAresta("a5", "v2-v8")

#V3
grafo.adicionaAresta("a6", "v3-v7")

# V4
grafo.adicionaAresta("a7", "v4-v5")
grafo.adicionaAresta("a8", "v4-v6")
grafo.adicionaAresta("a9", "v4-v12")

# V5
grafo.adicionaAresta("a10", "v5-v6")

# V6
grafo.adicionaAresta("a11", "v6-v7")
grafo.adicionaAresta("a12", "v6-v11")

# V7
grafo.adicionaAresta("a13", "v7-v8")
grafo.adicionaAresta("a14", "v7-v10")
grafo.adicionaAresta("a45", "v7-v11")

# V8
grafo.adicionaAresta("a15", "v8-v9")

# V9
grafo.adicionaAresta("a16", "v9-v16")

# V10
grafo.adicionaAresta("a17", "v10-v15")

# V11
grafo.adicionaAresta("a18", "v11-v12")
grafo.adicionaAresta("a19", "v11-v14")

# V12
grafo.adicionaAresta("a20", "v12-v13")

# V13
grafo.adicionaAresta("a21", "v13-v18")
grafo.adicionaAresta("a22", "v13-v20")

# V14
grafo.adicionaAresta("a23", "v14-v17")
grafo.adicionaAresta("a24", "v14-v18")
grafo.adicionaAresta("a25", "v14-v19")

# V15
grafo.adicionaAresta("a26", "v15-v18")

# V16
grafo.adicionaAresta("a27", "v16-v17")

# V17
grafo.adicionaAresta("a45", "v17-v18")

# V18
grafo.adicionaAresta("a28", "v18-v19")
grafo.adicionaAresta("a29", "v18-v23")
grafo.adicionaAresta("a30", "v18-v24")

# V19
grafo.adicionaAresta("a31", "v19-v20")
grafo.adicionaAresta("a32", "v19-v22")

# V20
grafo.adicionaAresta("a33", "v20-v21")

# V21
grafo.adicionaAresta("a34", "v21-v28")
grafo.adicionaAresta("a35", "v21-v29")
# V22
grafo.adicionaAresta("a36", "v22-v27")
grafo.adicionaAresta("a37", "v22-v28")

# V23
grafo.adicionaAresta("a38", "v23-v26")

# V24
grafo.adicionaAresta("a39", "v24-v25")
grafo.adicionaAresta("a40", "v24-v26")

# V25

# V26
grafo.adicionaAresta("a41", "v26-v31")

# V27

# V28

# V29
grafo.adicionaAresta("a42", "v29-v30")

# V30
grafo.adicionaAresta("a43", "v30-v31")

# V31
grafo.adicionaAresta("a44", "v31-v32")

# V32
grafo.adicionaAresta("a46", "v31-v33")

# V33


def criar(grafo):
    print("self.g_roteiro7 = Grafo([", end="")

    for v in grafo.N:
        print("\"" + v + "\"", end="")
        print(", ", end="")

    print("], ", end="")
    for a in grafo.A:
        print("\"" + a + "\":" + "\"" + grafo.A[a] + "\"", end="")
        print(",", end="")
    print("})")

print("Dak")
print(grafo.dakjastra("v1", "v32"))
print(grafo.dakjastraDrone("v6", "v32", 4,3, ["v9", "v18", "v21", "v30"]))

criar(grafo)