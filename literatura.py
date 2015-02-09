# -*- coding: utf-8 -*-
"""
Created on Sat Feb 07 21:30:44 2015 

@author: Grupo 7
"""
"""
Este algoritmo foi criado para que a procura seja efectuada não apenas no organismo em questão, mas sim em todo o Pubmed,
pois no caso em que nos interesse procurar um artigo sobre uma proteína obtida num Blast de outro organismo, o possamos fazer
directamente pelo Pyhton.
Realizado com base no tutorial Biopython
"""
from Bio import Entrez
from Bio import Medline


class Literatura:
	def __init__(self):
		self.record=[]
		self.idlist=[]
		
	def fetch_abstract(self,Titulo):
		Entrez.email = "jhmdf@hotmail.com"
		handle = Entrez.esearch(db = "pubmed", term = Titulo, retmax = 1)
		result= Entrez.read(handle)
		handle.close
		idlist=result["IdList"]
		handle2 = Entrez.efetch(db="pubmed", id=idlist, rettype="medline", retmode="text")
		result2 = Medline.parse(handle2)
		for record in result2:
			print(record["AB"])
		handle2.close()
	
	def Procura_artigos_termos(self,*args):
		Entrez.email = "jhmdf@hotmail.com"
		termos=''
		for termo in args:
			termos+=str(termo)
			termos+=str(' AND ')
		termos=termos.rsplit(' and ',1)[0]
		nartigos=raw_input("Introduza o numero maximo de artigos a procurar: ")
		handle = Entrez.esearch(db="pubmed", term=str(termos),retmax=nartigos)#para garantir que encontramos o máximo possível de artigos
		record=Entrez.read(handle)
		idlist=record["IdList"]
		self.idlist=idlist
		handle.close()
		handle2 = Entrez.efetch(db="pubmed", id=idlist, rettype="medline", retmode="text")
		record2=Medline.parse(handle2)
		record2=list(record2)
		self.record=record2
		handle2.close()
		
	def opcoes(self,*args):
		self.Procura_artigos_termos(*args)
		point=0
		final=5
		while final<=len(self.record)+5:
			if final>=(len(self.record)):
				final=(len(self.record))
			print "A apresentar os resultados",str(point+1),"-",str(final)
			for i in xrange(point,final):
				print "\n",str(i+1),"Title:",self.record[i].get("TI","?")
			print """\nEscolha de 1 a 5 pela ordem dos artigos o que artigo que pretende escolher
Escolha 6 para apresentar os proximos resultados e 7 para sair"""
			op=raw_input("Algum deste titulos interessa?")
			if op=="1":
				print "\n","Title:",self.record[point].get("TI","?"),"\n"
				self.fetch_abstract(self.record[point].get("TI","?"))
				print "\n","Caso o artigo interesse, este e o seu id no Pubmed:",self.idlist[point]
				op=raw_input("Pressione Enter para apresentar de novo os resultados")
			elif op=="2":
				if point+1<len(self.record):
					print "\n","Title:",self.record[point+1].get("TI","?"),"\n"
					self.fetch_abstract(self.record[point].get("TI","?"))
					print "\n","Caso o artigo interesse, este e o seu id no Pubmed:",self.idlist[point+1]
					op=raw_input("Pressione Enter para apresentar de novo os resultados")
				else:
					print "\nOpcao nao valida"
			elif op=="3":
				if point+2<len(self.record):
					print "\n","Title:",self.record[point+2].get("TI","?"),"\n"
					self.fetch_abstract(self.record[point].get("TI","?"))
					print "\n","Caso o artigo interesse, este e o seu id no Pubmed:",self.idlist[point+2]
					op=raw_input("Pressione Enter para apresentar de novo os resultados")
				else:
					print "\nOpcao nao valida"
			elif op=="4":
				if point+3<len(self.record):
					print "\n","Title:",self.record[point+3].get("TI","?"),"\n"
					self.fetch_abstract(self.record[point].get("TI","?"))
					print "\n","Caso o artigo interesse, este e o seu id no Pubmed:",self.idlist[point+3]
					op=raw_input("Pressione Enter para apresentar de novo os resultados")
				else:
					print "\nOpcao nao valida"
			elif op=="5":
				if final<len(self.record):
					print "\n","Title:",self.record[final].get("TI","?"),"\n"
					self.fetch_abstract(self.record[final].get("TI","?"))
					print "\n","Caso o artigo interesse, este e o seu id no Pubmed:",self.idlist[final]
					op=raw_input("Pressione Enter para apresentar de novo os resultados")
				else:
					print "\nOpcao nao valida"
			elif op=="6":
				if final==len(self.record):
					print "\nNao ha mais artigos, caso deseje mais, aumente o tamanho de procura"
					return
				point+=5
				final+=5
			elif op=="7":
				return
			else:
				print "\nOpcao nao valida"
		print "\nNao ha mais artigos, caso deseje mais, aumente o tamanho de procura"
#		while final<=len(self.record):
#			for i in xrange(len((point,final))):
#				print ("title:",lrecords.get("TI","?"))
#			op=input("Interessa algum titulo?")
		
		
if __name__ == '__main__':
	teste=Literatura()
	print """Ajuda para introducao dos termos de pesquisa:
Os termos devem estar dentro de " " e separados por , """
	terms=raw_input("Introduza os termos de procura: ")
	teste.opcoes(terms)
		
