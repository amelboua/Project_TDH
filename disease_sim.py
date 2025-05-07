import tkinter as tk
from tkinter import ttk

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class App:
  def __init__(self, root):
    #init window
    self.root = root
    self.root.title("Disease Spread Simulator") #Titre de fenetre
    self.graph_canvas = None #keep track of the current graph so we can delete it when another one is generated

    # init fonctions for sliders
    self.num_nodes = tk.IntVar(value=10)
    self.probability = tk.DoubleVar(value=0.3)

    self.patient_zero = tk.IntVar(value=0) #init patient zero

    self.create_widgets() #Fonction qui contient features of the window
  

  # The window features
  def create_widgets(self):
    ttk.Label(self.root, text="Disease Network Simulator").pack() # A small title

    #So we can enter a value to choose patient zero
    ttk.Label(self.root, text="Patient Zero (node ID):").pack()
    tk.Entry(self.root, textvariable=self.patient_zero).pack()


    ttk.Button(self.root, text="Generate Random Graph", command=self.generate_graph).pack() # add generate button and refrenece it to the generate function

    ttk.Button(self.root, text="Visualize Graph", command=self.visualize_graph).pack() # add visualize button and refrenece it to the generate function

    ttk.Button(self.root, text="Simulate Infection", command=self.simulate_infection).pack() # add simulate button and refrenece it to the generate function


    #number of nodes slider with label
    ttk.Label(self.root, text="Number of individuals:").pack()
    tk.Scale(self.root, from_=10, to=100, variable=self.num_nodes, orient="horizontal", command=self.update_node_label).pack()
    self.node_label = ttk.Label(self.root, text=f"Selected: {self.num_nodes.get()}")
    self.node_label.pack()


    #connectivity slider with label
    ttk.Label(self.root, text="Connection probability:").pack()
    tk.Scale(self.root, from_=0.0, to=1.0, resolution=0.01, variable=self.probability, orient="horizontal").pack()


  def generate_graph(self):
    #if graph exists, delete it (vefore generating a new one)
    if self.graph_canvas:
      self.graph_canvas.get_tk_widget().destroy()

    #choose number of nodes + connectivity
    n = self.num_nodes.get()
    p = self.probability.get()

    #input patient zero
    pz = self.patient_zero.get()
    #generate graph with inputed numbers
    G = nx.erdos_renyi_graph(n=n, p=p)

    #change color of patient zero
    node_colors = ['red' if node == pz else 'skyblue' for node in G.nodes]

    fig = plt.figure(figsize=(5,5))
    nx.draw(G, with_labels=True, node_color=node_colors, node_size=500, edge_color='gray')

    self.graph_canvas = FigureCanvasTkAgg(fig, master=self.root)
    self.graph_canvas.draw()
    self.graph_canvas.get_tk_widget().pack()

    #idk brother
  
  def visualize_graph(self):
    print("Visualizing graph...")
    
  def simulate_infection(self):
    print("Running infection simulation...")
  
  def update_node_label(self, event):
    self.node_label.config(text=f"Selected: {self.num_nodes.get()}")



root = tk.Tk()
root.geometry("800x600")
app = App(root)
root.mainloop()