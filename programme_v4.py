#!/usr/bin/env python3

def affiche_texte(letexte):
  """
  Fonction qui permet d'afficher le texte fourni en argument
  """
  print(letexte)

def demande_texte():
  """
  Fonction qui demande un mot à afficher à l'utilisateur, pour l'instant elle ne fait rien
  """
  pass

def main():
  demande_texte()
  affiche_texte("Coucou")
  affiche_texte("Bonjour")

if __name__ == "__main__":
  main()
