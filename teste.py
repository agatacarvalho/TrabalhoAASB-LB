from Bio import SeqIO
from Bio.Alphabet import IUPAC

#importar a tabela de codoes para bacterias
from Bio.Data import CodonTable

#funçao do complemento inverso
def reverse_complement(seq):
	compinv=seq.reverse_complement()
	return compinv

#funçao para o id, nome e descriçao do registo
def registos(record):
	ID=record.id
	nome=record.name
	descricao=record.description
	tamanho=len(record.seq)
	return ID, nome, descricao,tamanho

def anotacoes(record): #organismo e classificaçao taxonomica completa
	organismo=record.annotations['source']
	taxon=record.annotations['taxonomy']
	return organismo,taxon

#funçao para tipo e localizacao das features (geral)
def features(record):
	for feature in record.features:
		print "%s %s" % (feature.type, feature.location)

#funçao que indica o GeneID, nome dos genes 'curados' e as respectivas localizações e strands em que se encontram
def gene(record):
	gene=[]
	features=record.features
	for i in xrange(len(features)): 
		if features[i].type == "gene": 
			gene.append(i) 
	for k in gene: 
		print features[k].qualifiers.get('db_xref'), features[k].location, features[k].qualifiers.get('gene')

#funçao que indica as o nome dos diferentes produtos das CDS, o respectivo locus_tag e as localizações e strans em que se encontram
def product(record):
	cds=[]
	features=record.features
	for i in xrange(len(features)): 
		if features[i].type == "CDS": 
			cds.append(i) 
	for k in cds: 
		print features[k].qualifiers.get('locus_tag'),features[k].location, features[k].qualifiers.get('product') 
	
#funçao para a sequencia das diferentes CDS
def seq_cds(record):
	featcds = []
	features=record.features
	for i in xrange(len(features)): 
		if features[i].type == "CDS": 
			featcds.append(i) 
	for k in featcds: 
		print features[k].extract(record.seq) 
			
#funçao para extrair a sequencias das diferentes proteinas
def seq_protein(record):
	proteins = []
	features=record.features
	for i in xrange(len(features)):
		if features[i].type=="CDS":
			proteins.append(i)
	for k in proteins:
		print features[k].qualifiers.get('translation')

#funções para procurar determinados locus de interesse (locus_tag)
def find_locus(record,enzimas):
	features=record.features
	for f in features: 
		if f.type == "CDS" and "locus_tag" in f.qualifiers:
			locus=f.qualifiers["locus_tag"][0]
			if locus in enzimas:
				print f.qualifiers["locus_tag"][0],f.location,f.qualifiers["product"][0]

#sequencias, conversoes e tabelas
#leitura do ficheiro com a sequencia no formato genbank
record=SeqIO.read("sequence.gb","genbank",alphabet=IUPAC.ambiguous_dna)
#leitura do ficheiro com os locus_tag das enzimas citopasmaticas essenciais do patogeneo
locus=open("Essential_cytoplasmatic_enzimes.txt","r")
locus2=open("Essential_membrane_enzimes.txt","r")
locus3=open("Essential_membrane_transporters.txt","r")
locus4=open("candidate_targets.txt","r")
enzimas=locus.read()
enzimas2=locus2.read()
enzimas3=locus3.read()
enzimas4=locus4.read()
#regiao do genoma atribuida ao grupo (1422701 a 1657900 bp)
dna=record.seq
#regiao do genoma transcrito
rna=dna.transcribe()
#tabela de codoes de bacterias
bact_table= CodonTable.unambiguous_dna_by_id[11] #id para a tabela de bacterias


#main
#print record
#print enzimas
#print 'DNA: ' + dna
#print "RNA: " + rna
#print reverse_complement(dna)

#print "ID do registo: %s; nome do registo: %s; descricao do registo: %s; tamanho da sequencia: %s" %(registos(record))
#print "Organismo a que a sequencia pertence: %s; taxonomia completa do organismo: %s" %(anotacoes(record))
#features(record)
#gene(record)
#product(record)
#seq_cds(record)
#seq_protein(record)
find_locus(record,enzimas)
#find_locus(record,enzimas2)
#find_locus(record,enzimas3)
#find_locus(record,enzimas4)
